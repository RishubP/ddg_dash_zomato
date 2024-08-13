# index.py
from dash import dcc, html
from dash.dependencies import Input, Output
from app import app
from pages import homepage, page2

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
                Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/homepage':
        return homepage.layout
    elif pathname == '/page2':
        return page2.layout
    else:
        return homepage.layout  

if __name__ == '__main__':
    app.run_server(debug=True)