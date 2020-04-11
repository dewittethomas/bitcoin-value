import json
import requests

res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
json_data = json.loads(res.text)

def EUR():
    return "€" + str(round(json_data['bpi']['EUR']['rate_float'], 2))

def USD():
    return "$" + str(round(json_data['bpi']['USD']['rate_float'], 2))

def GBP():
    return "£" + str(round(json_data['bpi']['GBP']['rate_float'], 2))
