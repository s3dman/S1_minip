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

# def stock_info(stock):
#     ticker = yfinance.Ticker(stock)
#     x = ticker.info
#     if x == None:
#         return -1
#     d = {}
#     v = "Currentprice Volume".split()
#     for i in x:
#         if i not in v:
#             continue
#         if x[i] == None:
#             continue
#         d[i.title()] = x[i]
#     return d

def stock_info(stock):
    ticker = yfinance.Ticker(stock)
    x = dict(ticker.info)
    v = {}
    v["Current Price"] = f'${x["currentPrice"]}'
    v["Previous Close"] = f'{x["previousClose"]}'
    v["Day Range"] = f'${x["dayLow"]} - ${x["dayHigh"]}'
    v["Year Range"] = f'${x["fiftyTwoWeekLow"]} - ${x["fiftyTwoWeekHigh"]}'
    v["Market Cap"] = f'{int(x["marketCap"])/1e6:.3f}M USD'
    v["Volume"] = f'{int(x["volume"])/1e3:.3f}K'
    v["Summary"] = x['longBusinessSummary']
    return v

