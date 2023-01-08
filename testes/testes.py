import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import  dash_bootstrap_components as dbc

from datetime import datetime as dt
import plotly.graph_objs as go

app = dash.Dash()
app.layout =  dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
)
if __name__ == '__main__':
    app.run_server(debug=True)