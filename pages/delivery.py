import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import dash_table
from flask import request, Response,stream_with_context 
data = pd.read_csv('./data/zomato.csv', encoding = 'ISO-8859-1')
# print(data['Restaurant Name'].head(1))
from flask.globals import session
import dash
from dash import dcc, html
from flask import Flask, request

# server = Flask(__name__)
# # url = request.json["url"]
# print("URL:", request.url)

delivery_layout =html.Div(children =[
    html.Div(children=[
    dcc.Link(html.Img(
        src='/assets/images/logo.jpg',
        style={'height': '50px', 'marginRight': 'auto', 'padding': '20px'}
    ), href='/home'),
    html.Div([
        html.Img(src='/assets/images/cart.jpg', style={'height': '50px', 'padding': '20px'}),
        html.Img(src='/assets/images/profile.jpg', style={'height': '50px', 'padding': '20px'})
        
    ], style={'display': 'flex', 'marginLeft': 'auto'})
],
    style={'display': 'flex', 'alignItems': 'center'}),


    
    html.Div(children=[
                    html.Div(children=[
                                    html.Img(src='/assets/images/deli.jpg', style={
                                        'height': '40px',
                                        'marginLeft': '20px',
                                        'padding': '0px',  
                                        'border': 'none'
                                    }),
                                    html.Button('Delivery', style={
                                        'height': '40px',
                                        'backgroundColor': 'rgb(229, 228, 226, 0.1)',
                                        'border': 'none',
                                        'fontSize': '16px',
                                        'marginLeft': '10px', 
                                        'marginTop': '0px',  
                                        'fontWeight': 'bold',
                                        'color': '#D70040'
                                    })
                                    ], style={'display': 'flex', 'align-items': 'center'}),
    

                    html.Div(children=[
                        html.Img(src='/assets/images/dine1.jpg', style={
                            'height': '40px',
                            'marginLeft': '20px',
                            'padding': '0px', 
                            'border': 'none'
                        }),
                        dcc.Link(html.Button('Dining', style={
                            'height': '40px',
                            'backgroundColor': 'rgb(229, 228, 226, 0.1)',
                            'border': 'none',
                            'fontSize': '16px',
                            'color': '#71797E',
                            'marginLeft': '10px', 
                            'marginTop': '0px'  
                        }), href='/dining2')
                    ], style={'display': 'flex', 'align-items': 'center'}),
                    html.Div(children=[
                        html.Img(src='/assets/images/night.jpg', style={
                            'height': '40px',
                            'marginLeft': '20px',
                            'padding': '0px', 
                            'border': 'none'
                        }),
                        dcc.Link(html.Button('NightLife', style={
                            'height': '40px',
                            'backgroundColor': 'rgb(229, 228, 226, 0.1)',
                            'border': 'none',
                            'fontSize': '16px',
                            'color': '#71797E',
                            'marginLeft': '10px', 
                            'marginTop': '0px' 
                        }), href='/live2')
                    ], style={'display': 'flex', 'align-items': 'center'})
                ], style={
                    'backgroundColor': 'rgb(229, 228, 226, 0.1)',
                    'height': '50px',
                    'display': 'flex',
                    'marginTop': '10px',
                    'align-items': 'center'  
                })
                ,
    html.Div(children=[
                html.Div('Inspiration for your first order', style={'textAlign':'center', 'fontSize':'20px', 'marginTop':'20px'}),
                html.Div(children= [dcc.Link(html.Img(
                    src='/assets/images/conti.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/conti'),
                dcc.Link(html.Img(
                    src='/assets/images/burger.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                ,href = '/burger'),
                dcc.Link(html.Img(
                    src='/assets/images/indian.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/Indian'),
                dcc.Link(html.Img(
                    src='/assets/images/japan.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/japan'),
                dcc.Link(html.Img(
                    src='/assets/images/seafood.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/seafood'),
                dcc.Link(html.Img(
                    src='/assets/images/italian.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/italian'),
                dcc.Link(html.Img(
                    src='/assets/images/french.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/french'),
                dcc.Link(html.Img(
                    src='/assets/images/beverages.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/beverages'),
                dcc.Link(html.Img(
                    src='/assets/images/asian.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/asian')
                ], 
                style={'height':'200px','display':'flex','padding':'50px', 'textAlign':'center'})],
                style={'marginTop':'20px','backgroundColor':'white'}),
    
    html.Div(
        children=[
        html.H1('Delivering near you', style ={'textAlign':'center', 'display':'flex','justifyContent':'center', 'fontColor':'Grey', 'color':'#C41E3A'}),
            dcc.Input(
                id='delivery_search',
                type='text',
                placeholder='Search location or cuisines...',
                style={'width': '50%', 'fontSize': '16px', 'marginBottom': '20px', 'textAlign':'center', 'justifyContent':'center', 'display':'flex','marginLeft':'500px',
                       'border':'none','height':'40px'}
            ),
        # dash_table.DataTable(
        #     id='delivery_table',
        #     columns=[{"name": i, "id": i} for i in ['Restaurant Name','City', 'Cuisines','Average Cost for two','Rating text']],
        #     data=data[data["Is delivering now"] == "Yes"].to_dict('records'),
        #     style_table={'overflowX': 'auto','overflowY':'auto','padding':'50px', 'textAlign':'center', 'border':'None', 'backgroundColor':'white'},
        #     sort_action='native', filter_action = 'native',
        #     style_header={
        #         'backgroundColor': 'Red',
        #         'color': 'white',
        #         'textAlign': 'center',
        #         'fontWeight' :'bold',
        #         'fontSize':'18px'
        #     },
        #     style_cell={
        #         'height': 'auto',
        #         'minWidth': '80px', 'width': '80px', 'maxWidth': '80px',
        #         'whiteSpace': 'normal', 'textAlign':'center',
        #         'fontSize':'16px',
        #         'Color':'grey'
        #     },
        #    
        #         style_data_conditional=[{
        #                                 'if': {'row_index': 'odd'},
        #                                 'backgroundColor': 'rgb(220, 220, 220)'}
        #                             ]
        # ),
        html.Div(id = 'cards', style={'textAlign':'center','display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'space-between', 
                                       'backgroundColor':'white',  'marginTop':'30px' ,'paddingLeft':'150px','paddingRight':'150px', 'paddingTop':'20px'})
    ]
)])
