import requests

res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
json_data = res.json()

def EUR():
    return "€" + str(json_data['bpi']['EUR']['rate_float'])

def USD():
    return "$" + str(json_data['bpi']['USD']['rate_float'])

def GBP():
    return "£" + str(json_data['bpi']['GBP']['rate_float'])