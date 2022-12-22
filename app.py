import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(external_stylesheets=[dbc.themes.GRID])
suppress_callback_exceptions = True
server = app.server
