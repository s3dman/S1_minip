import yfinance
import yahoo_fin.stock_info as si

from urllib.request import urlopen
import json
import wikipedia
import local_dh
import multithread

def SymbolGetdh():
    url = "https://datahub.io/core/nasdaq-listings/r/nasdaq-listed-symbols.json"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

def stock_history_period(stock,period,interval,dateget=True):
    ticker=yfinance.Ticker(stock)
    history=ticker.history(interval=interval,period=period)
    if dateget:
        dates = [i.timestamp() for i in list(history.index)]
        if len(dates) == 0:
            return -1
        return dates,list(history["Open"]),list(history["High"]),list(history["Low"]),list(history["Close"])
    else:
        return list(history["Open"]),list(history["High"]),list(history["Low"]),list(history["Close"])


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

def ftwlh(stock):
    data = stock_history_period(stock,'1y','1d',dateget=False)
    return  [min(data[-1]),max(data[-1])]

def stock_info(stock,summary=True):
    # ticker = yfinance.Ticker(stock)
    # x = dict(ticker.info)
    # v = {}
    # v["Current Price"] = f'${x["currentPrice"]}'
    # v["Previous Close"] = f'${x["previousClose"]}'
    # v["Day Range"] = f'${x["dayLow"]} - ${x["dayHigh"]}'
    # v["Year Range"] = f'${x["fiftyTwoWeekLow"]} - ${x["fiftyTwoWeekHigh"]}'
    # v["Market Cap"] = f'{int(x["marketCap"])/1e6:.3f}M USD'
    # v["Volume"] = f'{int(x["volume"])/1e3:.3f}K'
    # v["Summary"] = x['longBusinessSummary']
    # return v

    data = si.get_quote_table(stock)
    db = local_dh.SymbolGet()
    currentPrice = float(data['Open'])
    previousClose = float(data['Previous Close'])
    dayLow,dayHigh = [float(i) for i in data["Day's Range"].split(" - ")]
    fiftyTwoWeekLow,fiftyTwoWeekHigh = [float(i) for i in data["52 Week Range"].split(" - ")]
    marketCap = data["Market Cap"]
    volume = float(data["Volume"])
    if summary:
        try:
            longBusinessSummary = wikipedia.summary(db[stock])
        except:
            longBusinessSummary = "Not found"
    else:
        longBusinessSummary = "Not found"

    v = {}
    v["Current Price"] = f'${currentPrice:.3f}'
    v["Previous Close"] = f'${previousClose:.3f}'
    v["Day Range"] = f'${dayLow:.3f} - ${dayHigh:.3f}'
    v["Year Range"] = f'${fiftyTwoWeekLow:.3f} - ${fiftyTwoWeekHigh:.3f}'
    v["Market Cap"] = f'{marketCap} USD'
    v["Volume"] = f'{int(volume)/1e3:.3f}K'
    v["Summary"] = longBusinessSummary
    return v
