from dash import Dash
from dash_flask_login_tpr import FlaskLoginAuth
import dash_bootstrap_components as dbc

app = Dash(__name__, suppress_callback_exceptions=True, assets_folder='assets')
server = app.server
app.url_base_pathname = "/"
app.title="Zomato"
# FlaskLoginAuth(app, use_default_views=True)