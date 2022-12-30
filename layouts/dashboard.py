from dash import html, callback_context
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc

tab_card = {
    'background-image': 'url("https://f.vividscreen.info/soft/ffcc63f4169b1a1efef560378a794c7c/Maserati-Quattroporte-tall-l.jpg")',
    'background-repeat': 'no-repeat',
    'height': '44vh',
    'background-size': '100% 100%',
    'opacity': '0.4',
    'border-radius': '20px'

    # 'margin-top': '50px'

}

dashboard = [
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col(style=tab_card),
                    ]),
                    html.Div([
                        html.P('Margin - Negativa'),
                        html.P('Margin - Negativa'),
                        html.P('Margin - Negativa'),
                        html.P('Margin - Negativa'),
                    ], style={'text-align': 'center', 'margin-top': '-320px'}),

                    # dbc.Row([
                    #     dbc.Col('green', style={'background': 'green'}),
                    # ]),
                    # dbc.Row([
                    #     dbc.Col('orange', style={'background': 'orange'}),
                    # ])
                ]),

            ])
        ], style={'border': '1px solid #FFFFFF', 'height': '45vh'},
            md=4),
        dbc.Col([
            html.Div([
                html.P('Margin - Negativa'),
                html.P('Margin - Negativa'),
                html.P('Margin - Negativa')
            ])
        ], md=4, style={'border': '1px solid #FFFFFF'}),
        dbc.Col([
            html.Div([
                html.P('Margin - Negativa'),
                html.P('Margin - Negativa'),
                html.P('Margin - Negativa')
            ])
        ], md=4, style={'border': '1px solid #FFFFFF'}),
    ],
        style={

            'margin-left': '5px',
            'margin-top': '10px',

        }),
    dbc.Row([
        dbc.Col(html.Div([
            html.P('Margin - Negativa'),
            html.P('Margin - Negativa'),
            html.P('Margin - Negativa')
        ], )
            , md=3, style={'border': '1px solid #FFFFFF', 'height': '49vh', }),
        dbc.Col(html.Div([
            html.P('Margin - Negativa'),
            html.P('Margin - Negativa'),
            html.P('Margin - Negativa')
        ], )
            , md=9, style={'border': '1px solid #FFFFFF', 'height': '49vh', }),
    ],
        style={
            'margin-left': '5px',
            'margin-top': '10px',
        }),

]
