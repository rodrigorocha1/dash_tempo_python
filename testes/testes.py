import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import  dash_bootstrap_components as dbc

from datetime import datetime as dt
import plotly.graph_objs as go

app = dash.Dash()
app.layout = dbc.Card(
    [
        dbc.CardImg(
            src="https://f.vividscreen.info/soft/ffcc63f4169b1a1efef560378a794c7c/Maserati-Quattroporte-tall-l.jpg",
            top=True,
            style={"opacity": 0.3},
        ),
        dbc.CardImgOverlay(
            dbc.CardBody(
                [
                    html.H4("Card title", className="card-title"),
                    html.P(
                        "An example of using an image in the background of "
                        "a card.",
                        className="card-text",
                    ),
                    dbc.Button("Go somewhere", color="primary"),
                ],
            ),
        ),
    ],
    style={"width": "18rem"},
)
if __name__ == '__main__':
    app.run_server(debug=True)