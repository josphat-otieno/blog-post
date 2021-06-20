from .models import Quote
import requests, json

url = "http://quotes.stormconsultancy.co.uk/random.json"


def get_random_quote():
    '''
    method to random quotes by consuming the http requests
    '''
    quote_response = requests.get(url).json()

    random_quote = Quote(quote_response.get("author"), quote_response.get("quote"))

    return random_quote
