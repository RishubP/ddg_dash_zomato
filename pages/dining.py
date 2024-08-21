import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import dash_table
import dash_ag_grid as dag

data = pd.read_csv('./data/zomato.csv', encoding = 'ISO-8859-1')
# print(data['Restaurant Name'].head(1))
print(data.columns)


dining_layout =html.Div(children =[
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
                    html.Div(children=[
                        html.Img(src='/assets/images/deli.jpg', style={
                            'height': '40px',
                            'marginLeft': '20px',
                            'padding': '0px', 
                            'border': 'none'
                        }),
                        dcc.Link(html.Button('Delivery', style={
                            'height': '40px',
                            'backgroundColor': 'rgb(229, 228, 226, 0.1)',
                            'border': 'none',
                            'fontSize': '16px',
                            'color': '#71797E',
                            'marginLeft': '10px', 
                            'marginTop': '0px'  
                        }), href='/delivery3')
                    ], style={'display': 'flex', 'align-items': 'center'}),
                        html.Img(src='/assets/images/dine1.jpg', style={
                                        'height': '40px',
                                        'marginLeft': '20px',
                                        'padding': '0px',  
                                        'border': 'none'
                                    }),
                                    html.Button('Dining', style={
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
                , href ='/conti2'),
                dcc.Link(html.Img(
                    src='/assets/images/burger.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                ,href = '/burger2'),
                dcc.Link(html.Img(
                    src='/assets/images/indian.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/Indian2'),
                dcc.Link(html.Img(
                    src='/assets/images/japan.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/japan2'),
                dcc.Link(html.Img(
                    src='/assets/images/seafood.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/seafood2'),
                dcc.Link(html.Img(
                    src='/assets/images/italian.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/italian2'),
                dcc.Link(html.Img(
                    src='/assets/images/french.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/french2'),
                dcc.Link(html.Img(
                    src='/assets/images/beverages.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/beverages2'),
                dcc.Link(html.Img(
                    src='/assets/images/asian.jpg',
                    style={'height': '150px', 'width':'150px','padding':'25px', 'borderRadius':'50%'})
                , href ='/asian2')
                ], 
                style={'height':'200px','display':'flex','padding':'50px', 'textAlign':'center'})],
                style={'marginTop':'20px','backgroundColor':'white'}),
    
    html.Div(
        children=[
        html.H1('Experience town\'s favourite..', style ={'textAlign':'center', 'display':'flex','justifyContent':'center', 'fontColor':'Grey', 'color':'#C41E3A'}),
            dcc.Input(
                id='dining_search',
                type='text',
                placeholder='Search location or cuisines...',
                style={'width': '50%', 'fontSize': '16px', 'marginBottom': '20px', 'textAlign':'center', 'justifyContent':'center', 'display':'flex','marginLeft':'500px',
                       'border':'none','height':'40px'}
            ),

        html.Div(children=[
        dag.AgGrid(
        id='ag-grid',
        columnDefs = [
    # {"headerName": "Restaurant ID", "field": "Restaurant ID", "sortable": True, "filter": True, "resizable": True},
    {"headerName": "Restaurant Name", "field": "Restaurant Name", "sortable": True, "filter": True, "resizable": True},
    # {"headerName": "Country Code", "field": "Country Code", "sortable": True, "filter": True, "resizable": True},
    {"headerName": "City", "field": "City", "sortable": True, "filter": True, "resizable": True},
    # {"headerName": "Address", "field": "Address", "sortable": True, "filter": True, "resizable": True},
    # {"headerName": "Locality", "field": "Locality", "sortable": True, "filter": True, "resizable": True},
    # {"headerName": "Locality Verbose", "field": "Locality Verbose", "sortable": True, "filter": True, "resizable": True},
    # {"headerName": "Longitude", "field": "Longitude", "sortable": True, "filter": True, "resizable": True},
    # {"headerName": "Latitude", "field": "Latitude", "sortable": True, "filter": True, "resizable": True},
    {"headerName": "Cuisines", "field": "Cuisines", "sortable": True, "filter": True, "resizable": True},
    {"headerName": "Average Cost for two", "field": "Average Cost for two", "sortable": True, "filter": True, "resizable": True, "editable": True},
    # {"headerName": "Currency", "field": "Currency", "sortable": True, "filter": True, "resizable": True},
    # {"headerName": "Has Table booking", "field": "Has Table booking", "sortable": True, "filter": True, "resizable": True},
    # {"headerName": "Has Online delivery", "field": "Has Online delivery", "sortable": True, "filter": True, "resizable": True},
    # {"headerName": "Is delivering now", "field": "Is delivering now", "sortable": True, "filter": True, "resizable": True},
    # {"headerName": "Switch to order menu", "field": "Switch to order menu", "sortable": True, "filter": True, "resizable": True},
    {"headerName": "Price Range", "field": "Price range", "sortable": True, "filter": True, "resizable": True},
    {"headerName": "Rating", "field": "Aggregate rating", "sortable": True, "filter": True, "resizable": True},
    # {"headerName": "Rating color", "field": "Rating color", "sortable": True, "filter": True, "resizable": True},
    {"headerName": "Customer Rating", "field": "Rating text", "sortable": True, "filter": True, "resizable": True},
    # {"headerName": "Votes", "field": "Votes", "sortable": True, "filter": True, "resizable": True},
]
,
        rowData=data[['Restaurant Name','City','Cuisines','Average Cost for two','Price range','Aggregate rating','Rating text']].to_dict('records'),  # Convert DataFrame to a list of dictionaries
        defaultColDef={"sortable": True, "filter": True, "resizable": True, "autoSizeColumns": True, "cellStyle": {"textAlign": "center"}},
        className="ag-theme-alpine", 
        style={"height": "500px", "width": "auto", "margin": "0 auto"} 
    ),
    html.Div(id='output')
],
style={'padding':'50px',
       'color':'red'})
    ]
)])
