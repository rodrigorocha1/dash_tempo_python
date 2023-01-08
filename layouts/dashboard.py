from dash import html, callback_context
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc
import datetime

DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

dia_atual = DIAS[datetime.datetime.now().weekday()], ' , ', datetime.datetime.now().strftime("%d/%m/%Y")

dashboard = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardImg(
                                src="../assets/wind.png",
                                top=True,
                                style={"opacity": 0.5,
                                       'height': '39vh'},
                            ),
                            dbc.CardImgOverlay(
                                dbc.CardBody(
                                    [
                                        html.P(dia_atual),
                                        dbc.InputGroup(
                                            [
                                                dbc.Input(placeholder='Digite a Cidade aqui',
                                                          style={'height': '20px',
                                                                 'background': 'transparent',
                                                                 'border': '1px solid #FFFFFF',
                                                                 'color': ' #FFFFFF',
                                                                 'font-size': '10px'}),
                                                dbc.Button('?', style={'height': '20px',
                                                                       'font-size': '10px'})
                                            ],
                                        ),

                                    ],
                                ),
                            ),
                        ],

                    )
                    , style={'border': '1px solid #FFFFFF',
                             'height': '40vh', },
                    md=4),
                dbc.Col(style={'border': '1px solid #FFFFFF',
                               'height': '40vh', }, md=4),
                dbc.Col(style={'border': '1px solid #FFFFFF',
                               'height': '40vh', }, md=4),

            ], style={'padding': '10px',
                      'margin': '10px 10px 10px 10px'}

        ),
        dbc.Row(
            [
                dbc.Col(style={'border': '1px solid #FFFFFF',
                               'height': '50px',
                               'height': '40vh'},
                        md=3),
                dbc.Col(style={'border': '1px solid #FFFFFF',
                               'height': '50px',
                               'height': '40vh'}, md=9)
            ], style={'padding': '10px',
                      'margin': '10px 10px 10px 10px'}
        ),
    ]
)
