from dash import html, callback_context
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc

barra_lateral = html.Div([
    dbc.Row(
        [
            dbc.Col(
                html.Img(src='../assets/dsh.png',
                         className='class-img'), md=2),
            dbc.Col(
                dbc.Button('Dashboard',
                           href='/layouts/dashboard',
                           className='class-botao-layout'
                           ),
                md=10)
        ]
    ),
    dbc.Row(
        [
            dbc.Col(
                html.Img(src='../assets/map.png',
                         className='class-img'), md=2, style={}, align='center'),
            dbc.Col(
                dbc.Button('Mapa',
                           href='/layouts/mapa',
                           className='class-botao-layout'
                           ),
                md=10)
        ]
    ),
    dbc.Row(
        [
            dbc.Col(
                html.Img(src='../assets/localizacao.png',
                         className='class-img'), md=2, style={}, align='center'),
            dbc.Col(
                dbc.Button('Localização',
                           href='/layouts/localizacao',
                           className='class-botao-layout'
                           ),
                md=10)
        ]
    ),
    dbc.Row(
        [
            dbc.Col(
                html.Img(src='../assets/calendar.png',
                         className='class-img'), md=2, style={}, align='center'),
            dbc.Col(
                dbc.Button('Calendário',
                           href='/layouts/calendario',
                           className='class-botao-layout'
                           ),
                md=10)
        ]
    )
], id='id_menu', )
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
