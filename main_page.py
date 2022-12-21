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

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.Card(
                    dbc.CardBody(
                        barra_lateral
                    ),
                )
            ], className='class-barra-lateral')

        ],  md=2),
        dbc.Col([
            dbc.Row([
                dbc.Col(html.Div('blue', style={'background': 'blue'}), md=4),
                dbc.Col(html.Div('red', style={'background': 'red'}), md=4),
                dbc.Col(html.Div('yellow', style={'background': 'yellow'}), md=4),

            ]),
            dbc.Row([
                dbc.Col(html.Div('pink', style={'background': 'pink'}), md=3),
                dbc.Col(html.Div('green', style={'background': 'green'}), md=9),

            ]),

        ],  md=10)

    ])

], fluid=True, style={'height': '100vh'})

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
