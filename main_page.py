from dash import callback_context, dcc, html
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc
from layouts.barra_lateral import barra_lateral

app.layout = html.Div([
    dbc.Row(
        [
            dbc.Col(
                barra_lateral

                , className='class-barra-lateral', width=2),
            dbc.Col("One of three columns"
                    , className='class-coluna-2', ),
        ]
    ),
])

if __name__ == "__main__":
    app.run_server(port=8051, debug=True)
