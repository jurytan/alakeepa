# make a call to the graph image API
# make http call with this request:
# https://api.keepa.com/graphimage?key=<KEEPA_TOKEN>&domain=1&asin=<ASIN_ID>&salesrank=1&width=600&height=300&yzoom=0&fba=1&fbm=1&salesrank=1&used=1

from dotenv import load_dotenv
import os
import requests

load_dotenv()
KEEPA_TOKEN = os.getenv('KEEPA_TOKEN')

def fetch_graph(asin_id):
    payload = {
        'asin': asin_id,
        'domain': 1,
        'fba': 1,
        'fbm': 1,
        'height': 300,
        'key': KEEPA_TOKEN,
        'salesrank': 1,
        'used': 1,
        'width': 600,
        'yzoom': 0
    }
    url = 'https://api.keepa.com/graphimage'
    response = requests.get(url, params=payload)
    return response