from dash import html, callback_context
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc

dashboard = [
    dbc.Row('1 linha',
            style={'background': 'red', 'margin-left': '10px',
                   'margin-top':
                       '10px', }),
    dbc.Row('2 linha',
            style={'background': 'green',
                   'margin-left': '10px',
                   'margin-top': '10px'}),

]
