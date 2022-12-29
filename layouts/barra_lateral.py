from dash import html, callback_context
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc

barra_lateral = html.Div([
    dbc.Row(
        [

            html.Img(src='../assets/dsh.png', className='class-img'),

            dbc.Button('Dashboard',
                       href='/layouts/dashboard',
                       # className='class-botao-layout'
                       ),

        ]
    ),
    # dbc.Row(
    #     [
    #         html.Img(src='../assets/map.png', className='class-img'),
    #         dbc.Button('Mapa', href='/layouts/mapa', className='class-botao-layout'),
    #
    #     ]
    # ),
    # dbc.Row(
    #     [
    #         html.Img(src='../assets/localizacao.png', className='class-img'),
    #         dbc.Button('Localização', href='/layouts/localizacao', className='class-botao-layout')
    #     ]
    # ),
    # dbc.Row(
    #     [
    #         html.Img(src='../assets/dsh.png', className='class-img'),
    #         dbc.Button('Calendário', href='/layouts/calendario', className='class-botao-layout')
    #     ]
    # ),
], id='menu')
