import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import dash_table

data = pd.read_csv('./data/zomato.csv', encoding = 'ISO-8859-1')
# print(data['Restaurant Name'].head(1))
print(data.columns)


dining_layout =html.Div(children =[
    dcc.Link(html.Img(
                    src='/assets/images/logo.png',
                    style={'height': '50px', 'marginRight': 'auto'}
                ), href = '/2home'),
                html.Div(children=[dcc.Link(html.Button('Delivery', style= {'height':'40px','backgroundColor':'Lightgrey','border':'none','fontSize':'16px',
                                                                            'marginLeft':'50px','padding':'20px'}), href='/del2'),
                                   html.Button('Dining', style= {'height':'40px','backgroundColor':'LightGrey','border':'none','fontSize':'16px', 'padding':'20px',
                                                                   'fontColor':'white','fontWeight':'bold','color':'White'})
                                   ,
                                   dcc.Link(html.Button('Live Events', style= {'height':'40px','backgroundColor':'Lightgrey','border':'none','fontSize':'16px','padding':'20px'}), href='/live3')]
                        , style = {'backgroundColor':'Lightgrey', 'height':'50px', 'display':'flex', 'marginTop':'10px'}),
    html.Div(children= [dcc.Link(html.Img(
                    src='/assets/images/pizza.jpg',
                    style={'height': '150px','width':'150px', 'padding':'25px', 'borderRadius':'50%'})
                , href ='/2pizza'),
                dcc.Link(html.Img(
                    src='/assets/images/burger.jpg',
                    style={'height': '150px','width':'150px','padding':'25px','borderRadius':'50%'})
                ,href = '/2burger'),
                dcc.Link(html.Img(
                    src='/assets/images/indian.jpg',
                    style={'height': '150px','width':'150px','padding':'25px','borderRadius':'50%'})
                , href ='/2Indian'),
                dcc.Link(html.Img(
                    src='/assets/images/sushi.jpg',
                    style={'height': '150px','width':'150px','padding':'25px','borderRadius':'50%'})
                , href ='/2sushi'),
                dcc.Link(html.Img(
                    src='/assets/images/seafood.jpg',
                    style={'height': '150px','width':'150px','padding':'25px','borderRadius':'50%'})
                , href ='/2seafood'),
                dcc.Link(html.Img(
                    src='/assets/images/pasta.jpg',
                    style={'height': '150px','width':'150px','padding':'25px','borderRadius':'50%'})
                , href ='/2pasta')], 
                style={'height':'200px','display':'flex','padding':'50px', 'textAlign':'center','marginLeft':'300px'}),
                html.Div(
    children=[
        html.H1('Dining Restaurants', style ={'textAlign':'center', 'display':'flex','justifyContent':'center', 'fontColor':'red', 'backgroundColor':'white'}),
            dcc.Input(
                id='dining_search',
                type='text',
                placeholder='Search location or cuisines...',
                style={'width': '50%', 'fontSize': '16px', 'marginBottom': '20px', 'textAlign':'center', 'justifyContent':'center', 'display':'flex','marginLeft':'500px'}
            ),
        dash_table.DataTable(
            id='dining_table',
            columns=[{"name": i, "id": i} for i in ['Restaurant Name','City', 'Cuisines','Average Cost for two','Rating text']],
            data=data[data['Has Table booking'] == "Yes"].to_dict('records'),
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
