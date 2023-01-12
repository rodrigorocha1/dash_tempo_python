from dash import html, callback_context, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import *
import dash_bootstrap_components as dbc
import datetime
from services.imageservice import ImageService

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
                                top=True,
                                style={"opacity": 0.5,
                                       'height': '39vh'},
                                id='id_image',
                            ),
                            dbc.CardImgOverlay(
                                dbc.CardBody(
                                    [

                                        html.P(dia_atual, style={'position': 'absolute',
                                                                 'top': '10px'}),
                                        html.Br(),
                                        dbc.InputGroup(
                                            [
                                                dbc.Input(placeholder='Digite a Cidade aqui',
                                                          style={'height': '20px',
                                                                 'background': 'transparent',
                                                                 'border': '1px solid #FFFFFF',
                                                                 'color': ' #FFFFFF',
                                                                 'font-size': '10px'},
                                                          id='id_cidade'),
                                                dbc.Button('🔍', style={'height': '20px',
                                                                       'font-size': '10px'},
                                                           n_clicks=0,
                                                           id='id_botao_teste')
                                            ], style={'top': '-15px'}
                                        )
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
    Output('id_image', 'src'),
    Input('id_botao_teste', 'n_clicks'),
    State('id_cidade', 'value'))
def update_image_src(n_clicks, id_cidade):
    ctx = callback_context
    if n_clicks == 0:
        raise PreventUpdate
    else:

        text_img = ctx.states_list[0].get('value')

        img = ImageService()
        url_img = img.get_img(text_img)
        return url_img
