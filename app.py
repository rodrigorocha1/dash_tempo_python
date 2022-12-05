import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__)
app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True
server = app.server