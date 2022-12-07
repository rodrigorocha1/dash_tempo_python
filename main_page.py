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



app.layout = html.Div(
    [

        dbc.Row(
            [
                dbc.Col(html.Div("One of four columns"), md=2, sm=6, style={'background': 'red', 'height': '100vh'}),
                dbc.Col(html.Div("One of four columns"), md=10, sm=6, style={'background': 'blue'}),

            ]
        ),
    ]
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
