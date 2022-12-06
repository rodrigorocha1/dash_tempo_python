from dash import html, callback_context
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc

barra_lateral = [html.Img(src='assets/wind.png', className='class-img-barra-lateral', id='id_img_wind'),
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

                 ]), ]
