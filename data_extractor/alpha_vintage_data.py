import requests
import pandas as pd

API_KEY = "" #TODO: move this to environment variable

def load_intraday(symbol)-> pd.DataFrame:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=60min&apikey={API_KEY}'
    r = requests.get(url)
    return pd.DataFrame(r.json()['Time Series (60min)']).T.rename(columns={"1. open": "Open", "2. high":"High","3. low":"Low", "4. close": "Close", "5. volume": "Volume"})

if __name__ == "__main__":
    print(load_intraday("QCOM"))