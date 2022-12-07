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

app.layout = html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    html.Img(src='../assets/wind.png', className='class-img-barra-lateral', id='id_img_wind'),
                    html.P("Tempo agora", id='id_txt_tempo_agora'),
                    dcc.Location(id='url'),
                    barra_lateral,
                ]
                , className='class-barra-lateral', width=2),
            dbc.Col(
                html.Div(id="page-content")
            ),
        ]
    ),
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def carregar_pagina(pathname):
    if pathname == '/' or pathname == '/layouts/dashboard':
        return dashboard
    if pathname == '/' or pathname == '/layouts/mapa':
        return mapa
    if pathname == '/' or pathname == '/layouts/localizacao':
        return localizacao
    if pathname == '/' or pathname == '/layouts/calendario':
        return calendario


if __name__ == "__main__":
    app.run_server(port=8051, debug=True)
