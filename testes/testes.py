app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.Div(
                                [
                                    dbc.Col(html.Img(src='../assets/wind.png',
                                                     className='class-img')),
                                    dbc.Col(html.P('Tempo Agora',
                                                   className='id_txt_tempo_agora',
                                                   style={'color': '#2AA312'})),

                                ], id='cabecalho'
                            ),
                            dcc.Location(id="url"),
                            barra_lateral
                        ]
                    ),
                )
            ], className='class-barra-lateral')
        ], md=2,style={'margin-top': '10px'}),
        dbc.Col([
            html.Div(id="page-content")
        ], md=10
            # style={'padding' : '10px'}
        )
    ])
], fluid=True, style={'height': '100vh'})