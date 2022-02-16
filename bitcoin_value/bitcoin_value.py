import requests

def currency(currency=""):
    if currency != "":
        url = f"https://api.coindesk.com/v1/bpi/currentprice/{currency}.json"

        req = requests.get(url)

        if req.status_code == 404:
            raise ValueError(f"Currency {currency} does not exist.")
        elif req.status_code == 200:
            result = req.json()
            value = result["bpi"][f"{currency}"]["rate_float"]

            return float(value)

    else:
        raise ValueError("Currency is not defined.")