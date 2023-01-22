import yfinance

from urllib.request import urlopen
import json

def SymbolGetdh():
    url = "https://datahub.io/core/nasdaq-listings/r/nasdaq-listed-symbols.json"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

def stock_history_period(stock,period,interval):
    ticker=yfinance.Ticker(stock)
    history=ticker.history(interval=interval,period=period)
    dates = [i.timestamp() for i in list(history.index)]
    if len(dates) == 0:
        return -1
    return dates,list(history["Open"]),list(history["High"]),list(history["Low"]),list(history["Close"])

def stock_info(stock):
    ticker = yfinance.Ticker(stock)
    x = ticker.info
    if x == None:
        return -1
    d = {}
    for i in x:
        if x[i] == None:
            continue
        d[i.title()] = x[i]
    return d
