import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import dash_table
from page2 import delivery_layout
from homepage import home_layout
from app import app



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Delivery':
        return  delivery_layout
    # elif pathname == '/Dining':
    #     return dining_layout
    # elif pathname == '/Live':
    #     return dining_layout
    # elif pathname == '/home':
    #     return layout
    # elif pathname =='/pizza':
    #     return delivery_layout
    # elif pathname =='/pasta':
    #     return delivery_layout
    # elif pathname =='/sushi':
    #     return delivery_layout
    # elif pathname =='/seafood':
    #     return delivery_layout
    # elif pathname =='/Indian':
    #     return delivery_layout
    # elif pathname =='/burger':
    #     return delivery_layout
    # else:
    #     return home_layout()
    

@app.callback(Output('page-content', 'children'),
                Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/homepage':
        return home_layout()
    elif pathname == '/page2':
        return delivery_layout()
    else:
        return home_layout()