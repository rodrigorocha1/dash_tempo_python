from dash import html, callback_context
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc

mapa = dbc.Col(html.Div("mapa", className='class-linha-grande',
                        style={'background-color': 'blue'})
               )
