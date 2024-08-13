from dash import html, dcc

layout = html.Div([
    html.Div(
        id='header',
        style={
        'backgroundImage': 'url(https://b.zmtcdn.com/web_assets/81f3ff974d82520780078ba1cfbd453a1583259680.png)',
        'backgroundSize': 'cover',
        'backgroundPosition': 'center center',
        # 'height': '100%'  # Adjust the height as needed
        },
        children=[
            html.Div(
                className='logo',
                children=html.Img(src='https://b.zmtcdn.com/images/logo/zomato_flat_bg_logo.svg', height='50px')
            ),
            html.Div(
                className='search-bar',
                children=dcc.Input(id='search-input', type='text', placeholder='Search for restaurant, cuisine or a dish')
            ),
            html.Div(
                className='user-options',
                children=[
                    html.A('Login', href='#', className='login-link'),
                    html.A('Sign up', href='#', className='signup-link')
                ]
            )
        ]
    ),
    html.Div(
        id='main-content',
        children=[
            html.H1('Discover the best food & drinks'),
            html.Div(
                className='location-selector',
                children=[
                    dcc.Dropdown(
                        id='location-dropdown',
                        options=[
                            {'label': 'Delhi NCR', 'value': 'delhi_ncr'},
                            {'label': 'Mumbai', 'value': 'mumbai'},
                            {'label': 'Bangalore', 'value': 'bangalore'}
                        ],
                        placeholder='Select your city'
                    )
                ]
            ),
            html.Div(
                id='cuisines',
                children=[
                    html.H2('Popular Cuisines'),
                    html.Ul(
                        id='cuisine-list',
                        children=[
                            html.Li('Pizza'),
                            html.Li('Burger'),
                            html.Li('Sushi'),
                            html.Li('Chinese'),
                            html.Li('Indian')
                        ]
                    )
                ]
            ),
            html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Link(
                            html.Div(children =[
                            html.Button(
                                '',
                                id='delivery_button',
                                style={'fontSize': '24px', 'backgroundColor': '#fafafa',
                                       'backgroundImage': 'url("/assets/images/del.jpg")', 
                                       'backgroundSize': 'cover', 'backgroundRepeat': 'no-repeat', 'padding': '150px 150px', 'border': 'None','borderRadius':'20px',
                                       'textAlign': 'left', 'verticalAlign':'top'}
                            ),
                            html.Div('Deliver food at home',
                                     style={'fontSize':'16px', 'fontColor':'Red', 'textDecoration':'none'})],
                                     style={'padding':'5px', 'border':'2px solid grey',
                                            'borderRadius':'10px', 'textDecoration':'none',
                                            'fontWeight':'bold'}),
                            href='/Delivery'
                        )
                    ],
                    style={'textAlign': 'center', 'margin': '10px', 'alignItems':'flexStart' }
                ),
                html.Div(
                    children=[
                        dcc.Link(
                            html.Div(children = [
                            html.Button(
                                '',
                                id='dining_button',
                                style={'fontSize': '24px', 'backgroundColor': '#fafafa', 
                                        'backgroundImage': 'url("/assets/images/dine.jpg")', 'backgroundSize': 'cover', 'backgroundRepeat': 'no-repeat',
                                        'padding': '150px 150px', 'border': 'None','borderRadius':'20px'}
                            )
                            ,
                        html.Div('Favourite dining venues of the city',
                                 style={'fontSize':'16px', 'fontColor':'Red', 'textDecoration':'none'})
                        ], 
                        style={'padding':'5px', 'border':'2px solid grey',
                                            'borderRadius':'20px', 'textDecoration':'none',
                                            'fontWeight':'bold'}),
                            href='/Dining'
                        )]                    ,
                    style={'textAlign': 'center', 'margin': '10px',}
                ),
                html.Div(
                    children=[
                        dcc.Link(
                            html.Div(children = [
                            html.Button(
                                '',
                                id='events_button',
                                style={'fontSize': '24px', 'backgroundColor': '#fafafa', 
                                       'backgroundImage': 'url("/assets/images/live.jpg")', 'backgroundSize': 'cover', 'backgroundRepeat': 'no-repeat',
                                       'padding': '150px 150px', 'border': 'None', 'borderRadius':'20px'}
                            ),
                            html.Div('Live Music',
                                 style={'fontSize':'16px', 'fontColor':'Red', 'textDecoration':'none'})
                        ], 
                        style={'padding':'5px', 'border':'2px solid grey',
                                            'borderRadius':'20px', 'textDecoration':'none',
                                            'fontWeight':'bold'}),
                            href='/Live'
                        )
                    ],
                    style={'textAlign': 'center', 'margin': '10px', }
                )
            ],
            style={'justifyContent': 'center', 'marginTop': '50px', 'alignItems': 'center', 'display': 'flex'}
        )
        ]
    )
])