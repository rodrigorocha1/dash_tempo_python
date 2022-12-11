from dash import callback_context, dcc, html
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc
from layouts.barra_lateral import barra_lateral
from layouts.dashboard import dashboard
from layouts.mapa import mapa
from layouts.localizacao import localizacao
from layouts.calendario import calendario

content = html.Div(id="page_content")

app.layout = html.Div(children=[
    dbc.Row([
        dbc.Col(
            [
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4("Title", className="card-title"),
                            html.H6("Card subtitle", className="card-subtitle"),
                            html.P(
                                "Some quick example text to build on the card title and make "
                                "up the bulk of the card's content.",
                                className="card-text",
                            ),
                            dbc.CardLink("Card link", href="#"),
                            dbc.CardLink("External link", href="https://google.com"),
                        ]
                    ),
                )
            ],
            style={'height': '90vh'}, className='class-barra-lateral',
            sm=2,
        ),
        dbc.Col(
            [
                dbc.Row(
                    [
                        dbc.Col('Card 1 Linha 1', className='class-card-city', ),
                        dbc.Col('Card 2 Linha 1', className='class-card-sol', ),
                        dbc.Col('Card 3 Linha 1', className='class-intervalo-tempo'),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col('Card 1 Linha 1', id='id_direcao_vento', ),
                        dbc.Col('Card 2 Linha 1', id='coluna_mapa', ),

                    ],
                    style={'margin-top': '24px'}

                ),
            ],

            sm=10,
        ),

    ])
], style={'padding': '15px'}

)

# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def carregar_pagina(pathname):
#     if pathname == '/' or pathname == '/layouts/dashboard':
#         return dashboard
#     if pathname == '/' or pathname == '/layouts/mapa':
#         return mapa
#     if pathname == '/' or pathname == '/layouts/localizacao':
#         return localizacao
#     if pathname == '/' or pathname == '/layouts/calendario':
#         return calendario
#
#
if __name__ == "__main__":
    app.run_server(port=8051, debug=True)
