from dash import html, callback_context
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc

barra_lateral = dbc.Row([
    dbc.Col([
        html.Img(src='../assets/dsh.png', className='class-img-dash', id='botao_dash'),
        html.Img(src='../assets/map.png', className='class-img-map', id='botao_map'),
        html.Img(src='../assets/localizacao.png', className='class-img-loc', id='botao_localizacao'),
        html.Img(src='../assets/calendar.png', className='class-img-cal', id='botao_calendar'),

    ]),
    dbc.Col(
        dbc.Nav(
            [
                dbc.NavLink('Dashboard', href='/layouts/dashboard', active='exact'),
                dbc.NavLink('Mapa', href='/layouts/mapa', active='exact'),
                dbc.NavLink('Localização', href='/layouts/localizacao', active='xact'),
                dbc.NavLink('Calendário', href='/layouts/calendario', active='exact')
            ], id='nav_buttons', vertical='md'),
        width=8, style={'margin-top': '80px'}, ),

])
