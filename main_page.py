from dash import callback_context, dcc, html
from dash.dependencies import Input, Output, State
from app import *

app.layout = html.Div([

])

if __name__ == "__main__":
    app.run_server(port=8051, debug=True)