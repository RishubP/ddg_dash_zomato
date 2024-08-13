import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from dash import dash_table



delivery_layout =html.Div(children =[
    dcc.Link(html.Img(
                    src='/assets/images/bcn.png',
                    style={'height': '50px', 'marginRight': 'auto'}
                ), href = '/home'),
    html.Div(children= [dcc.Link(html.Img(
                    src='/assets/pizza.jpg',
                    style={'height': '100px', 'padding':'10px'})
                , href ='/pizza'),
                dcc.Link(html.Img(
                    src='/assets/burger.jpg',
                    style={'height': '100px','padding':'10px'})
                ,href = '/burger'),
                dcc.Link(html.Img(
                    src='/assets/indian.jpg',
                    style={'height': '100px','padding':'10px'})
                , href ='/Indian'),
                dcc.Link(html.Img(
                    src='/assets/sushi.jpg',
                    style={'height': '100px','padding':'10px'})
                , href ='/sushi'),
                dcc.Link(html.Img(
                    src='/assets/seafood.jpg',
                    style={'height': '100px','padding':'10px'})
                , href ='/seafood'),
                dcc.Link(html.Img(
                    src='/assets/pasta.jpg',
                    style={'height': '100px','padding':'10px'})
                , href ='/pasta')], 
                style={'height':'100px','display':'flex','padding':'50px', 'textAlign':'center','marginLeft':'400px'}),
                html.Div(
    children=[
        html.H1('Delivery Restaurants', style ={'textAlign':'center', 'display':'flex','justifyContent':'center', 'fontColor':'red'}),
            dcc.Input(
                id='delivery_search',
                type='text',
                placeholder='Search location or cuisines...',
                style={'width': '50%', 'fontSize': '16px', 'marginBottom': '20px', 'textAlign':'center', 'justifyContent':'center', 'display':'flex','marginLeft':'500px'}
            ),
        dash_table.DataTable(
            id='delivery_table',
            columns=[{"name": i, "id": i} for i in ['Restaurant Name','City', 'Cuisines','Average Cost for two','Rating text']],
            data=data[data["Is delivering now"] == "Yes"].to_dict('records'),
            style_table={'overflowX': 'auto','overflowY':'auto','padding':'50px', 'textAlign':'center', 'border':'None'},
            sort_action='native', filter_action = 'native',
            style_header={
                'backgroundColor': 'red',
                'color': 'white',
                'textAlign': 'center',
                'fontWeight' :'bold',
                'fontSize':'18px'
            },
            style_cell={
                'height': 'auto',
                'minWidth': '80px', 'width': '80px', 'maxWidth': '80px',
                'whiteSpace': 'normal', 'textAlign':'center',
                'fontSize':'16px',
                'Color':'grey'
            }
        )
    ]
)])