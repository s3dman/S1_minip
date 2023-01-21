import yfinance
import pandas as pd

from urllib.request import urlopen
import json

def SymbolGetdh():
    url = "https://datahub.io/core/nasdaq-listings/r/nasdaq-listed-symbols.json"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

# def stock_range_fetch(stock,info,start,stop,interval):
#     ticker=yfinance.Ticker(stock)
#     history=ticker.history(interval=interval,start=start,end=stop)
#     d = dict(history[info])
#     x,y = [],[]
#     for i in d:
#         x.append(i.to_pydatetime())
#         y.append(d[i])
#     return x,y
#         # i.to_pydatetime(),x[i])
#

def stock_range_fetch(stock,start,stop,interval):
    ticker=yfinance.Ticker(stock)
    history=ticker.history(interval=interval,start=start,end=stop)
    return [i.value/1e6 for i in list(history.index)],list(history["Open"]),list(history["High"]),list(history["Low"]),list(history["Close"])
    # return [i.value/1e6 for i in list(history.index)],list(history["Open"]),list(history["High"]),list(history["Low"]),list(history["Close"]),history["Volume"],history["Dividends"]
    
# stock_range_fetch("MSFT","2011-01-01","2023-01-01","1mo")
