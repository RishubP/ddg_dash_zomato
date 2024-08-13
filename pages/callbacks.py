import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import dash_table
from pages.delivery import delivery_layout
from pages.dining import dining_layout
from pages.homepage import layout
from app import app

data = pd.read_csv('./data/zomato.csv', encoding= 'ISO-8859-1')

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Delivery':
        return  delivery_layout
    elif pathname == '/Dining':
        return dining_layout
    # elif pathname == '/Live':
    #     return dining_layout
    elif pathname == '/home':
        return layout
    elif pathname =='/pizza':
        return delivery_layout
    elif pathname =='/pasta':
        return delivery_layout
    elif pathname =='/sushi':
        return delivery_layout
    elif pathname =='/seafood':
        return delivery_layout
    elif pathname =='/Indian':
        return delivery_layout
    elif pathname =='/burger':
        return delivery_layout
    elif pathname =='/2pizza':
        return dining_layout
    elif pathname =='/2pasta':
        return dining_layout
    elif pathname =='/2sushi':
        return dining_layout
    elif pathname =='/2seafood':
        return dining_layout
    elif pathname =='/2Indian':
        return dining_layout
    elif pathname =='/2burger':
        return dining_layout
    else:
        return layout
    

@app.callback(
    Output('delivery_table', 'data'),
    [Input('delivery_search', 'value'),
     Input('url','pathname')]
)
def update_table(search_value, pathname):
    filtered_data = data[data["Is delivering now"] == "Yes"]
    if search_value:
        filtered_data = filtered_data[
            filtered_data['City'].str.contains(search_value, case=False, na=False) |
            filtered_data['Locality'].str.contains(search_value, case=False, na=False) |
            filtered_data['Cuisines'].str.contains(search_value, case=False, na=False)
        ]
    if pathname=='/pizza':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Continental", case=False, na=False)]
    elif pathname=='/pasta':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Italian", case=False, na=False)]
    elif pathname=='/sushi':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Japanese", case=False, na=False)]
    elif pathname=='/Indian':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Indian", case=False, na=False)]
    elif pathname=='/seafood':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Sea", case=False, na=False)]
    elif pathname=='/burger':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Continental", case=False, na=False)]
    else:
        filtered_data
        
    return filtered_data.to_dict('records')


@app.callback(
    Output('dining_table', 'data'),
    [Input('dining_search', 'value'),
     Input('url','pathname')]
)
def update_table(search_value, pathname):
    filtered_data = data[data["Has Table booking"] == "Yes"]
    if search_value:
        filtered_data = filtered_data[
            filtered_data['City'].str.contains(search_value, case=False, na=False) |
            filtered_data['Locality'].str.contains(search_value, case=False, na=False) |
            filtered_data['Cuisines'].str.contains(search_value, case=False, na=False)
        ]
    if pathname=='/2pizza':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Continental", case=False, na=False)]
    elif pathname=='/2pasta':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Italian", case=False, na=False)]
    elif pathname=='/2sushi':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Japanese", case=False, na=False)]
    elif pathname=='/2Indian':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Indian", case=False, na=False)]
    elif pathname=='/2seafood':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Sea", case=False, na=False)]
    elif pathname=='/2burger':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Continental", case=False, na=False)]
    else:
        filtered_data
        
    return filtered_data.to_dict('records')



# @app.callback(Output('page-content', 'children'),
#                 Input('url', 'pathname'))
# def display_page(pathname):
#     if pathname == '/homepage':
#         return home_layout()
#     elif pathname == '/page2':
#         return delivery_layout()
#     else:
#         return home_layout()