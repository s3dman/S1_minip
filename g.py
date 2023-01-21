import yfinance as yf

i=input("INTERVAL IN FORMAT OF-[1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]:")
st=input("starting date(year-month-date):")
sp=input("end date(year-month-date):")
stock_name=input("enter stock name:")

stock=yf.Ticker(stock_name)
a=stock.history(interval=i,start=st,end=sp)
print(a)
a.to_csv("stockinfo.csv")



#valid intervals - [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
