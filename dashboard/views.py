from django.shortcuts import render
import dash
from dash import html
from dash import dcc
from . import app
import dash_bootstrap_components as dbc
import pandas as pd
from dash_bootstrap_templates import ThemeSwitchAIO




def dashboard_view(request):
   
    # Crie uma instância do aplicativo Dash
    FONT_AWESOME = ["https:/use.fontawesome.com/releases/v5.10.2/css/all.css"]
    dash_app = dash.Dash(__name__, external_stylesheets=FONT_AWESOME)
    dash_app.scripts.config.serve_locally = True
    server = dash_app.server 

    # ========== Reading and cleaning File ======#
    df = pd.read_csv('dataset_asimov.csv')
    df_cru = df.copy()

    # Meses em numeros para poupar memoria

    df.loc[ df['Mês'] == 'Jan', 'Mês'] = 1
    df.loc[ df['Mês'] == 'Fev', 'Mês'] = 2
    df.loc[ df['Mês'] == 'Mar', 'Mês'] = 3
    df.loc[ df['Mês'] == 'Abr', 'Mês'] = 4
    df.loc[ df['Mês'] == 'Mai', 'Mês'] = 5
    df.loc[ df['Mês'] == 'Jun', 'Mês'] = 6
    df.loc[ df['Mês'] == 'Jul', 'Mês'] = 7
    df.loc[ df['Mês'] == 'Ago', 'Mês'] = 8
    df.loc[ df['Mês'] == 'Set', 'Mês'] = 9
    df.loc[ df['Mês'] == 'Out', 'Mês'] = 10
    df.loc[ df['Mês'] == 'Nov', 'Mês'] = 11
    df.loc[ df['Mês'] == 'Dez', 'Mês'] = 12

    # Algumas limpezas
    df['Valor Pago'] = df['Valor Pago'].str.lstrip('R$ ')
    df.loc[df['Status de Pagamento'] == 'Pago', 'Status de Pagamento'] = 1
    df.loc[df['Status de Pagamento'] == 'Não pago', 'Status de Pagamento'] = 0

    # Transformando em int tudo que der
    df['Chamadas Realizadas'] = df['Chamadas Realizadas'].astype(int)
    df['Dia'] = df['Dia'].astype(int)
    df['Mês'] = df['Mês'].astype(int)
    df['Valor Pago'] = df['Valor Pago'].astype(int)
    df['Status de Pagamento'] = df['Status de Pagamento'].astype(int)


    # Criando opções para os filtros
    options_month = [{'label': 'Ano todo', 'value': 0}]
    for i, j in zip(df_cru['Mês'].unique(), df['Mês'].unique()):
        options_month.append({'label': i, 'value': j})
        options_month = sorted(options_month, key=lambda x: x['value'])    

    options_team = [{'label': 'Todas Equipes', 'value': 0}]
    for i in df['Equipe'].unique():
        options_team.append({'label': i, 'value': i})



    # ========== Styles ============ #
    tab_card = {'height': '100%'}
    config_graph={"displayModeBar": False, "showTips": False}
    url_theme1 = dbc.themes.FLATLY
    url_theme2 = dbc.themes.DARKLY

    
   
    # Defina o layout da sua dashboard
    app.layout = dbc.Container(children=[
    
    # Row 1
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([  
                                html.Legend("Sales Analytics")
                            ], sm=8),
                            dbc.Col([        
                                html.I(className='fa fa-balance-scale', style={'font-size': '300%'})
                            ], sm=4, align="center")
                        ]),
                        dbc.Row([
                            dbc.Col([
                                ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2]),
                                html.Legend("Asimov Academy")
                            ])
                        ], style={'margin-top': '10px'}),
                        dbc.Row([
                            dbc.Button("Visite o Site", href="https://asimov.academy/", target="_blank")
                        ], style={'margin-top': '10px'})
                    ])
                ], style=tab_card)
            ], sm=4, lg=2),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row(
                            dbc.Col(
                                html.Legend('Top Consultores por Equipe')
                            )
                        ),
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='graph1', className='dbc', config=config_graph)
                            ], sm=12, md=7),
                            dbc.Col([
                                dcc.Graph(id='graph2', className='dbc', config=config_graph)
                            ], sm=12, md=5)
                        ])
                    ])
                ], style=tab_card)
            ], sm=12, lg=7),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row(
                            dbc.Col([
                                html.H5('Escolha o Mês'),
                                dbc.RadioItems(
                                    id="radio-month",
                                    options=options_month,
                                    value=0,
                                    inline=True,
                                    labelCheckedClassName="text-success",
                                    inputCheckedClassName="border border-success bg-success",
                                ),
                                html.Div(id='month-select', style={'text-align': 'center', 'margin-top': '30px'}, className='dbc')
                            ])
                        )
                    ])
                ], style=tab_card)
            ], sm=12, lg=3)
        ], className='g-2 my-auto', style={'margin-top': '7px'}),

        # Row 2
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                dcc.Graph(id='graph3', className='dbc', config=config_graph)
                            ])
                        ], style=tab_card)
                    ])
                ]),
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                dcc.Graph(id='graph4', className='dbc', config=config_graph)
                            ])
                        ], style=tab_card)
                    ])
                ], className='g-2 my-auto', style={'margin-top': '7px'})
            ], sm=12, lg=5),
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                dcc.Graph(id='graph5', className='dbc', config=config_graph)    
                            ])
                        ], style=tab_card)
                    ], sm=6),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                dcc.Graph(id='graph6', className='dbc', config=config_graph)    
                            ])
                        ], style=tab_card)
                    ], sm=6)
                ], className='g-2'),
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dcc.Graph(id='graph7', className='dbc', config=config_graph)
                        ], style=tab_card)
                    ])
                ], className='g-2 my-auto', style={'margin-top': '7px'})
            ], sm=12, lg=4),
            dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph8', className='dbc', config=config_graph)
                ], style=tab_card)
            ], sm=12, lg=3)
        ], className='g-2 my-auto', style={'margin-top': '7px'}),
        
        # Row 3
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4('Distribuição de Propaganda'),
                        dcc.Graph(id='graph9', className='dbc', config=config_graph)
                    ])
                ], style=tab_card)
            ], sm=12, lg=2),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Valores de Propaganda convertidos por mês"),
                        dcc.Graph(id='graph10', className='dbc', config=config_graph)
                    ])
                ], style=tab_card)
            ], sm=12, lg=5),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='graph11', className='dbc', config=config_graph)
                    ])
                ], style=tab_card)
            ], sm=12, lg=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5('Escolha a Equipe'),
                        dbc.RadioItems(
                            id="radio-team",
                            options=options_team,
                            value=0,
                            inline=True,
                            labelCheckedClassName="text-warning",
                            inputCheckedClassName="border border-warning bg-warning",
                        ),
                        html.Div(id='team-select', style={'text-align': 'center', 'margin-top': '30px'}, className='dbc')
                    ])
                ], style=tab_card)
            ], sm=12, lg=2),
        ], className='g-2 my-auto', style={'margin-top': '7px'})
    ], fluid=True, style={'height': '100vh'})


    # Renderize a dashboard como uma string HTML
    dashboard_html = dash_app.index()

    # Renderize o template Django com a string HTML da dashboard
    return render(request, 'dashboard.html', {'dashboard_html': dashboard_html})
