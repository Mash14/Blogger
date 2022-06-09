# urllib.request module helps create connection to the API URl and send a request
# json module will format the JSON response to a python dictionary
import urllib.request,json

# ur  class from models.py 
from .models import Quotes

# Getting the quotes base url
base_url = None

def configure_request(app):
    # from the config
    global base_url
    base_url = app.config['QUOTES_API_BASE_URL']

# Your code here

def get_quotes():
    
    with urllib.request.urlopen(base_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

    return get_quotes_response 