import pandas as pd
import dash

# Type 'dev' if you are in development environment. Before deploying, change it to 'prod'
ENV = 'prod'
app = dash.Dash(__name__)
server = app.server
hotel_data = pd.read_csv('data/hotel_data.csv')

if ENV == 'dev':
    debug = True
else:
    debug = False


""" Version with SQL engine and database in Heroku. Private information hidden """
"""
from sqlalchemy import create_engine

if ENV == 'dev':
    debug = True
    hotel_data = pd.read_csv('data/hotel_data.csv')
else:
    debug = False
    engine = create_engine(
        'postgres://fyyrkpoootwwip:96a16f82e35538a99569bcbbe92e1f0710a38e60af267091d2e391c8e6ec7daf@ec2-34-197-141-7.compute-1.amazonaws.com:XXXX/XXXXXXXXXX')
    uri = 'postgres://fyyrkpoootwwip:96a16f82e35538a99569bcbbe92e1f0710a38e60af267091d2e391c8e6ec7daf@ec2-34-197-141-7.compute-1.amazonaws.com:XXXX/XXXXXXXXXX'
    hotel_data = pd.read_sql_table("hoteldashboard", con=uri)
"""


""" 
For an online version of the css layout 
external_stylesheets = ['https://codepen.io/davifoga/pen/ROVzra.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
"""
