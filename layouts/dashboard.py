from dash import html, callback_context
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc

dashboard = html.Div(
    [
        dbc.Row([
            dbc.Col(
                dbc.Card([

                ], className='class-card-city')
            ),
            dbc.Col(
                dbc.Card([

                ], className='class-card-sol')
            ),
            dbc.Col(
                dbc.Card([

                ], className='class-intervalo-tempo')

            ),
        ]),
        dbc.Row([
            dbc.Col(
                dbc.Card([

                ], id='id_direcao_vento', ) ,
            ),
            dbc.Col(
                id='coluna_mapa',
            ),

        ]),
    ]
),
