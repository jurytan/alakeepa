# make a call to the graph image API
# make http call with this request:
# https://api.keepa.com/graphimage?key=<yourAccessKey>&domain=<domainId>&asin=<ASIN>

# https://api.keepa.com/graphimage?key=<KEEPA_TOKEN>&domain=1&asin=<ASIN_ID>&salesrank=1&width=600&height=300&yzoom=0&fba=1&fbm=1&salesrank=1&used=1

from dotenv import load_dotenv
import os
import requests

load_dotenv()
KEEPA_TOKEN = os.getenv('KEEPA_TOKEN')
ASIN_ID = 'B08HFSLPQJ'

def fetch(asin_id):
    url = 'https://api.keepa.com/graphimage?key=' + KEEPA_TOKEN + '&domain=1&asin='+ asin_id + '&salesrank=1&width=600&height=300&yzoom=0&fba=1&fbm=1&salesrank=1&used=1'
    f = requests.get(url)

    # for 400, check the json error.type/message/details and pass that back to the user
    # for 200, it will always return an PNG image, even if the ASIN is incorrect
