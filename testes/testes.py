import datetime

import dash
from dash import callback_context
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import flask
import glob
import os
from app import *

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

app.layout =  html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardImg(
                                top=True,
                                src='../assets/dsh.png',
                                style={"opacity": 0.5,
                                       'height': '39vh'},
                                id='id-image',
                            ),
                            dbc.CardImgOverlay(
                                dbc.CardBody(
                                    [
                                        html.P(dia_atual),
                                        html.Br(),
                                        dbc.InputGroup(
                                            [
                                                dbc.Input(placeholder='Digite a Cidade aqui',
                                                          style={'height': '20px',
                                                                 'background': 'transparent',
                                                                 'border': '1px solid #FFFFFF',
                                                                 'color': ' #FFFFFF',
                                                                 'font-size': '10px'},
                                                          id='id-cidade'),
                                                dbc.Button('?', style={'height': '20px',
                                                                       'font-size': '10px'},
                                                           id='id-botao-teste')
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

@app.callback(
    Output('id-image', 'src'),
    [Input('id-botao-teste', 'n_clicks')],
    [State('id-cidade', 'value')])
def update_image_src(*_):
    ctx = callback_context
    print('ctx.inputs', ctx.inputs)
    print('ctx.states', ctx.states)
    print('ctx.states_list', ctx.states_list[0].get('value'))
    print('ctx.inputs', ctx.inputs)
    path_img = ctx.states_list[0].get('value')
    # path_img = f'/assets/{ctx.states_list[0].get("value")}'
    # print(path_img)
    return path_img


# Add a static image route that serves images from desktop
# Be *very* careful here - you don't want to serve arbitrary files
# from your computer or server


if __name__ == '__main__':
    app.run_server(debug=True, port=8087)
