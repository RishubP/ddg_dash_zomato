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
    if pathname == '/delivery3':
        return  delivery_layout
    elif pathname == '/Dining':
        return dining_layout
    # elif pathname == '/Live':
    #     return dining_layout
    elif pathname == '/home':
        return layout
    elif pathname =='/conti':
        return delivery_layout
    elif pathname =='/italian':
        return delivery_layout
    elif pathname =='/japan':
        return delivery_layout
    elif pathname =='/seafood':
        return delivery_layout
    elif pathname =='/Indian':
        return delivery_layout
    elif pathname =='/burger':
        return delivery_layout
    elif pathname =='/french':
        return delivery_layout
    elif pathname =='/beverages':
        return delivery_layout
    elif pathname =='/asian':
        return delivery_layout
    elif pathname =='/conti2':
        return dining_layout
    elif pathname =='/italian2':
        return dining_layout
    elif pathname =='/japan2':
        return dining_layout
    elif pathname =='/seafood2':
        return dining_layout
    elif pathname =='/Indian2':
        return dining_layout
    elif pathname =='/burger2':
        return dining_layout
    elif pathname =='/french2':
        return dining_layout
    elif pathname =='/beverages2':
        return dining_layout
    elif pathname =='/asian2':
        return dining_layout
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
    elif pathname =='/dining2':
        return dining_layout
    elif pathname =='/live2':
        return layout
    elif pathname =='/del2':
        return delivery_layout
    elif pathname =='/live3':
        return layout
    else:
        return layout
    

# @app.callback(
#     Output('delivery_table', 'data'),
#     [Input('delivery_search', 'value'),
#      Input('url','pathname')]
# )
# def update_table(search_value, pathname):
#     filtered_data = data[data["Is delivering now"] == "Yes"]
#     if search_value:
#         filtered_data = filtered_data[
#             filtered_data['City'].str.contains(search_value, case=False, na=False) |
#             filtered_data['Locality'].str.contains(search_value, case=False, na=False) |
#             filtered_data['Cuisines'].str.contains(search_value, case=False, na=False) |
#             filtered_data['Restaurant Name'].str.contains(search_value, case=False, na=False)
#         ]
#     if pathname=='/pizza':
#         filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Continental", case=False, na=False)|filtered_data['Cuisines'].str.contains("Italian", case=False, na=False)]
#     elif pathname=='/pasta':
#         filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Italian", case=False, na=False)]
#     elif pathname=='/sushi':
#         filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Japanese", case=False, na=False)]
#     elif pathname=='/Indian':
#         filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Indian", case=False, na=False)]
#     elif pathname=='/seafood':
#         filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Sea", case=False, na=False)]
#     elif pathname=='/burger':
#         filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Continental", case=False, na=False)]
#     else:
#         filtered_data
        
#     return filtered_data.to_dict('records')


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
            filtered_data['Cuisines'].str.contains(search_value, case=False, na=False) |
            filtered_data['Restaurant Name'].str.contains(search_value, case=False, na=False)
        ]
    if pathname=='/2pizza':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Continental", case=False, na=False)|filtered_data['Cuisines'].str.contains("Italian", case=False, na=False)]
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


@app.callback(
    Output('cards', 'children'),
    Input('delivery_search', 'value'),
    Input('url','pathname')
)
def update_cards(search_value, pathname):
    filtered_data = data[data["Is delivering now"] == "Yes"]
    if search_value:
        filtered_data = filtered_data[
            filtered_data['City'].str.contains(search_value, case=False, na=False) |
            filtered_data['Locality'].str.contains(search_value, case=False, na=False) |
            filtered_data['Cuisines'].str.contains(search_value, case=False, na=False) |
            filtered_data['Restaurant Name'].str.contains(search_value, case=False, na=False)
        ]
    if pathname=='/conti':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Continental", case=False, na=False)|filtered_data['Cuisines'].str.contains("Italian", case=False, na=False)]
    elif pathname=='/italian':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Italian", case=False, na=False)]
    elif pathname=='/japan':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Japanese", case=False, na=False)]
    elif pathname=='/Indian':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Indian", case=False, na=False)]
    elif pathname=='/seafood':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Sea", case=False, na=False)]
    elif pathname=='/burger':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Continental", case=False, na=False)]
    elif pathname=='/french':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("French", case=False, na=False)]
    elif pathname=='/beverages':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Beverages", case=False, na=False)]
    elif pathname=='/asian':
        filtered_data = filtered_data[filtered_data['Cuisines'].str.contains("Asian", case=False, na=False)]
    else:
        filtered_data


    cards = []
    for index, row in filtered_data.iterrows():

        if row['Rating text'] == 'Excellent':
            button_color = 'rgb(76, 175, 80)'  
            rating = 'Excellent ★★★★'
        elif row['Rating text'] == 'Good':
            button_color = 'rgb(255, 193, 7)'  
            rating = 'Good ★★★'
        elif row['Rating text'] == 'Average':
            button_color = 'rgb(250, 160, 160)' 
            rating = 'Average ★★'
        elif row['Rating text'] == 'Poor':
            button_color = 'rgb(244, 67, 54)'
            rating = 'Poor ★'
        else:
            button_color = 'rgb(189, 189, 189)' 

        if (("Continental" in row['Cuisines']) & ("Fast Food" not in row["Cuisines"])):
            src = '/assets/images/test.jpg'
        elif "Japanese" in row['Cuisines']:
            src = '/assets/images/sushi.jpg'
        elif "Mexican" in row['Cuisines']:
            src = '/assets/images/mexican.jpg'
        elif "Mughlai" in row['Cuisines']:
            src = '/assets/images/mughlai.jpg'
        elif "Sea" in row['Cuisines']:
            src = '/assets/images/seafood.jpg'
        elif "Biryani" in row['Cuisines']:
            src = '/assets/images/biryani.jpg'
        elif "Chinese" in row['Cuisines']:
            src = '/assets/images/chinese.jpg'
        elif 'South' in row['Cuisines']:
            src = '/assets/images/south.jpg'
        elif "Indian" in row['Cuisines']:
            src = '/assets/images/Indian.jpg'
        elif "Peruvian" in row['Cuisines']:
            src = '/assets/images/peru.jpg'
        elif "Asian" in row['Cuisines']:
            src = '/assets/images/asian.jpg'
        elif "Beverages" in row['Cuisines']:
            src = '/assets/images/beverages.jpg'
        elif "Desserts" in row['Cuisines']:
            src = '/assets/images/dessert.jpg'
        elif "Bakery" in row['Cuisines']:
            src = '/assets/images/cake.jpg'
        elif "French" in row['Cuisines']:
            src = '/assets/images/french.jpg'
        elif "Cafe" in row['Cuisines']:
            src = '/assets/images/tea.jpg'

        else:
            src =  '/assets/images/food.jpg'

        

        card = html.Div(
            [
                html.H4(row['Restaurant Name'], style={'margin-bottom': '10px', 'color':'#800000','fontSize':'24px'}),
                html.Div(
                    children = [
                                html.P(f"City: {row['City']}", style={'margin': '0','textAlign':'left'}),
                                html.Button(f"{rating}", style={'backgroundColor':button_color, 'border':'none','textAlign':'right',
                                                                'borderRadius':'4px'})
                    ],
                    style = {'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center'}
                ),
                 html.Div(
                    children = [
                html.P(f"Cost for two: {row['Average Cost for two']}", style={'margin': '0', 'textAlign':'left'}),
                html.P(f"{row['Cuisines']}", style={'margin': '0', 'textAlign':'right','marginLeft':'50px',
                                                    'fontStyle':'italic'}),
                ],
                    style = {'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center'}
                ),
                html.Img(
                    src=src,
                      style={
                            'height': '40%',  # or any fixed height you prefer
                            'width': '100%',
                            'padding': 'none',
                            'marginTop': '5px',
                            'object-fit': 'cover',  # Ensures the image covers the area while maintaining aspect ratio
                            'object-position': 'center' , # Centers the image within the allocated space
                            'border-radius': '0 0 5px 5px'
                        }),
                html.Div(f"Locality: {row['Locality']}", style={'margin': '0','textAlign':'left','marginTop':'10px'})
            ],
            style={
                'border': '1px solid #ccc',
                'padding': '10px',
                'margin-bottom': '10px',
                'border-radius': '5px',
                'box-shadow': '#9d5757 2px 2px 5px',
                'background-color': 'rgb(250, 160, 160, 0.05)',
                'width': '25%',
                'height': '300px',  # Make height auto to fit content
                'overflow': 'hidden' 
                # 'textAlign':'center'
            }
        )
        cards.append(card)
    
    return cards

@app.callback(
    Output('ag-grid', 'rowData'),
    [Input('dining_search', 'value')]
)
def filter_table(search_value):
    if not search_value:
        return data.to_dict('records')

    if search_value:
        filtered_data = data[
            data['City'].str.contains(search_value, case=False, na=False) |
            data['Locality'].str.contains(search_value, case=False, na=False) |
            data['Cuisines'].str.contains(search_value, case=False, na=False) |
            data['Restaurant Name'].str.contains(search_value, case=False, na=False)
        ]
    
    return filtered_data.to_dict('records')