import json
import requests

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
json_data = json.loads(response.text)

def EUR():
    return "€" + str(json_data['bpi']['EUR']['rate_float']).replace(".", ",")

def USD():
    return "$" + str(json_data['bpi']['USD']['rate_float']).replace(".", ",")

def GBP():
    return "£" + str(json_data['bpi']['GBP']['rate_float']).replace(".", ",")