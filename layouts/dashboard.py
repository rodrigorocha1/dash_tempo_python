from dash import html, callback_context
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc

dashboard = html.Div(
    [
        dbc.Row([
            dbc.Col(html.Div('blue', className='class-card-city'), md=4),  # style={'background': 'blue'}
            dbc.Col(html.Div('red', className='class-card-sol'), md=4),
            dbc.Col(html.Div('yellow', className='class-intervalo-tempo'), md=4),

        ], style={'margin-top': '10px'}),
        dbc.Row([
            dbc.Col(html.Div('pink', id='id_direcao_vento'), md=3),
            dbc.Col(html.Div('green', id='coluna_mapa'), md=9),
        ], style={'margin-top': '10px'})
    ]
),


