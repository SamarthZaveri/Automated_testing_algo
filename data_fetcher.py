import yfinance as yf
import pandas as pd


STOCKS = ["RELIANCE.NS", "INFY.NS", "TCS.NS"]


def fetch_data(period="6mo", interval="1d"):
    data = {}
    for stock in STOCKS:
        df = yf.download(stock, period=period, interval=interval)
        df.dropna(inplace=True)
        data[stock] = df
        return data