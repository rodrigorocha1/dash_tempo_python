from dash import callback_context, dcc, html
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc

app.layout = html.Div([
    dbc.Row(
        [
            dbc.Col([
                html.Img(src='assets/wind.png', className='class-img-barra-lateral', id='id_img_wind'),
                html.P("Tempo agora", id='id_txt_tempo_agora'),

                dbc.Row([
                    dbc.Col([
                        html.Img(src='assets/dsh.png', className='class-img-dash'),
                        html.Img(src='assets/map.png', className='class-img-map'),
                        html.Img(src='assets/localizacao.png', className='class-img-loc'),
                        html.Img(src='assets/calendar.png', className='class-img-cal'),

                    ]),
                    dbc.Col(
                        [
                            dbc.Button('Dashboard', className='class-botao-layout'),
                            dbc.Button('Mapa', className='class-botao-layout'),
                            dbc.Button('Localizaçao', className='class-botao-layout'),
                            dbc.Button('Calendario', className='class-botao-layout'),
                        ],
                        width=8, style={'margin-top': '80px'}, ),

                ]),

            ], className='class-barra-lateral', width=2),
            dbc.Col("One of three columns"
                    , className='class-coluna-2', ),
        ]
    ),
])

if __name__ == "__main__":
    app.run_server(port=8051, debug=True)
