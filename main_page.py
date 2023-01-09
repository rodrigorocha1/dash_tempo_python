from dash import callback_context, dcc, html
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc
from layouts.dashboard import dashboard
from layouts.mapa import mapa
from layouts.localizacao import localizacao
from layouts.calendario import calendario

search_bar = dbc.Row(
    [
        dbc.Nav(
            children=[

                dbc.NavItem(
                    dbc.NavLink(' 📝 ' + 'Dashboard',
                                href='/layouts/dashboard',

                                className='class-link-dsb',
                                style={'color': '#FFFFFF'},
                                id='id-pg-dashboard'
                                )
                ),
                dbc.NavItem(
                    dbc.NavLink(' 🗺️ ' + 'Mapa',
                                href='/layouts/mapa',
                                className='class-link-mapa',
                                style={'color': '#FFFFFF'},
                                id='id-pg-mapa'

                                )
                ),
                dbc.NavItem(
                    dbc.NavLink(' 📍 ' + 'Localização',
                                href='/layouts/localizacao',
                                className='class-link-loc',
                                style={'color': '#FFFFFF'}
                                )
                ),
                dbc.NavItem(
                    dbc.NavLink(' 📅 ' + 'Calendário',
                                href='/layouts/calendario',
                                className='class-link-cal',
                                id='id-pg-calendario',
                                style={'color': '#FFFFFF'}
                                )
                ),
            ],
        )
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",

)

app.layout = html.Div(
    [
        dcc.Location(id='url'),
        dbc.Navbar(
            dbc.Container(
                [
                    html.A(
                        # Use row and col to control vertical alignment of logo / brand
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Img(src='assets/windy-line.png',
                                             height="30px")
                                ),
                                dbc.Col(
                                    dbc.NavbarBrand("Tempo Agora",
                                                    className="ms-2",
                                                    style={'color': '#FFFFFF'}
                                                    )
                                ),
                            ],
                            align="center",
                            className="g-0",
                        ),
                    ),
                    dbc.NavbarToggler(
                        id="navbar-toggler",
                        n_clicks=0
                    ),
                    dbc.Collapse(
                        search_bar,
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                    ),
                ]
            ),
            color="primary",
        ),
        html.Div(id='page-content')
    ]
)


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def render_page_content(pathname):
    if pathname == '/layouts/dashboard' or pathname == '/':
        return dashboard
    elif pathname == '/layouts/mapa':
        return mapa
    elif pathname == '/layouts/localizacao':
        return localizacao
    elif pathname == '/layouts/calendario':
        return calendario
    else:
        return '404'


if __name__ == "__main__":
    app.run_server(port=8044, debug=True)
