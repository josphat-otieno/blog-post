import urllib.request,json
from .models import Quote

quote_url = "http://quotes.stormconsultancy.co.uk/random.json"


def get_random_quote():
 

    with urllib.request.urlopen(quote_url) as url:
        random_quote_data=url.read()
        random_quote_response= json.loads(random_quote_data)

        author=random_quote_response.get('author')
        quote=random_quote_response.get('quote')

        quote= Quote(author,quote)

        return quote