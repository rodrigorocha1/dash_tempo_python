from dash import html, callback_context
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc


dashboard = dbc.Col(html.Div("dashboard", className='class-linha-grande',
                             style={'background-color': 'blue'})
                    )