import yfinance
import pandas as pd

from urllib.request import urlopen
import json

def SymbolGetdh():
    url = "https://datahub.io/core/nasdaq-listings/r/nasdaq-listed-symbols.json"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

def stock_range_fetch(stock,info,start,stop,interval):
    ticker=yfinance.Ticker(stock)
    history=ticker.history(interval=interval,start=start,end=stop)
    x = dict(history[info])
    return x
        # i.to_pydatetime(),x[i])

x = stock_range_fetch("MSFT","High","2022-01-01","2023-01-01","1mo")
