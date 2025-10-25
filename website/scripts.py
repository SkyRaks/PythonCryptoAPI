import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

API_KEY = "your api key"
base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

# this is api call for cryptocurrency data
def get_crypto_data():
    parameters = {
        'start': '1',
        'limit': '10',
        'convert': 'USD'
    }

    headers = {
        'Content-Type': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY,
    }

    try:
        responce = requests.get(url=base_url, headers=headers, params=parameters)
        data =responce.json()
        crypto_data = data.get("data", [])
        print(f"status code: {responce.status_code}")
        return crypto_data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        crypto_data = []
        print(e)
    return crypto_data
