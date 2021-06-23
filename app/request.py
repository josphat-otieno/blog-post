import requests

from .models import Quote

url = "http://quotes.stormconsultancy.co.uk/random.json"


def get_random_quote():
    '''
    method to random quotes by consuming the quotes API
    '''
    quote_response = requests.get(url).json()

    random_quote = Quote(quote_response.get("author"), quote_response.get("quote"))

    return random_quote
