import requests

class currency():
    def __init__(self, currency=""):

        if currency != "":
            self.currency = currency
            self.url = f"https://api.coindesk.com/v1/bpi/currentprice/{self.currency}.json"
        else:
            raise ValueError("Currency is not defined.")

    def fetch(self):

        res = requests.get(self.url)
      
        if res.status_code == 404:
            raise ValueError(f"Currency {self.currency} does not exist.")
        elif res.status_code == 200:
            data = res.json()
            value = data["bpi"][f"{self.currency}"]["rate_float"]

            return value