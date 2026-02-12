import requests


def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        return data["bitcoin"]["usd"]

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None
