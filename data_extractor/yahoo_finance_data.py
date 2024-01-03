import pandas as pd
from datetime import datetime
import yfinance as yf
from time_utils import Period, Interval
from typing import List
import json

""""
Get text to perform sentiment analysis and other text related reports
"""
def load_data_for_analysis():
    pass

"""
Load historycal data. This is mainly used to train the time series model
"""
def load_historical_data(interval:Interval, symbols:List[str], pediod: Period = Period.MAX)-> pd.DataFrame:
    try:
        return yf.download(tickers=symbols, period=str(pediod), interval=str(interval))
    except:
        return pd.DataFrame()

"""
Intraday data cannot extend last 60 days on yahoo API
"""
def load_intraday(symbol, interval = Interval.HOUR)-> pd.DataFrame:
    try:
        return yf.download(tickers=symbol, period=str(Period.DAY), interval=str(interval))
    except:
        return pd.DataFrame()
    

def download_historical_data():
    with open('tickers.json', '+r') as tickers_list:
        tickers = [t['stock'] for t in json.load(tickers_list)]
        yf.download(tickers=tickers, period=str(Period.MAX), interval=str(Interval.DAY)).to_excel("training_data/historical_data.xlsx")


if __name__ == "__main__":
    download_historical_data()
    # yf.download(tickers=['MSFT','QCOM'], period=str(Period.MAX), interval=str(Interval.DAY)).to_excel("historical_example.xlsx")
    # data = yf.download(tickers='QCOM', period=str(Period.WEEK), interval=str(Interval.HOUR))
    # print(data)
    # data.index = data.index.apply(lambda a: pd.to_datetime(a).date()) 

    # data.to_json("yahoo_finance_intraday_sample.json",)
    # print(load_historical_data(pediod=Period.WEEKLY, interval= Interval.WEEK, stock= "MSFT"))