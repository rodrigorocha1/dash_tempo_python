from dash import callback_context, dcc, html
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc
from layouts.barra_lateral import barra_lateral
from layouts.dashboard import dashboard
from layouts.mapa import mapa
from layouts.localizacao import localizacao
from layouts.calendario import calendario

app.layout = dbc.Container(
    children=[
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col(
                                [
                                    dcc.Location(id="url"),
                                    barra_lateral
                                ],
                                className='class-barra-lateral',
                                md=2),
                            dbc.Col(
                                html.Div(id="page-content"), md=10),
                        ]),
                        # dbc.Row([
                        #     dbc.Col('green', style={'background': 'green'}),
                        # ]),
                        # dbc.Row([
                        #     dbc.Col('orange', style={'background': 'orange'}),
                        # ])
                    ])
                ])
            ]),
        ]),
    ]
)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def render_page_content(pathname):
    print(pathname)
    if pathname == '/layouts/dashboard' or pathname == '/':
        return dashboard
    elif pathname == '/layouts/mapa':
        return mapa
    elif pathname == '/layouts/localizacao':
        return localizacao
    else:
        return calendario


if __name__ == "__main__":
    app.run_server(port=8051, debug=True)
