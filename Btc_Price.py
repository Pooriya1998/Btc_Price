import requests
import json
import pyttsx3


class coindesk:
    def get_btc_price(self):
        res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = json.loads(res.text)
        b_price = (data['bpi']['USD']['rate'])

        btc_price = int(float(b_price.replace(',','')))
        return btc_price

