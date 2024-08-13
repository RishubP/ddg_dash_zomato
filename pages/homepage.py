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
                    className='user-options',
                    children=[
                        html.A('Login', href='#', className='login-link', style={'color':'white'}),
                        html.A('Sign up', href='#', className='signup-link', style={'color':'white'})
                    ]
                ),

            #   children=html.Img(src='https://b.zmtcdn.com/images/logo/zomato_flat_bg_logo.svg', height='50px')

                html.Div(
                    className='logo',
                    children=html.Img(src="https://b.zmtcdn.com/web_assets/8313a97515fcb0447d2d77c276532a511583262271.png", height='50px')
                ),
                html.Div(
                    className='discover-text',
                    children=html.H1("Discover the best food & drinks in ")
                ),
                html.Div(
                    className='search-bar',
                    children=dcc.Input(id='search-input', type='text', placeholder='Search for restaurant, cuisine or a dish')
                ),
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
            )
        ]
    )
])