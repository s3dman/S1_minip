import yfinance 
# import plotly.graph_objects as go
# import plotly.express as px

import datetime
a=datetime.date.today()

sta=input("enter starting date(year-month-date):")
stp=input("enter ending date(year-month-date):")
i=input("enter interval()[1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]:")
t=input("enter financial info to be plotted:")
s=input('enter stock name:')

tata=yfinance.Ticker(s)
hist=tata.history(interval=i,start=sta,end=stp)
print(hist.index)
print(hist[t])

# print(hist.head())

# df=px.data.iris()
# fig = px.scatter(x="Timeline", y="StockPrice", color="species",
#                 title="Stock Data")



# fig=go.Figure(data=go.Scatter(x=hist.index,y=hist[t],mode='lines+markers',xaxis="timeline",yaxis="High"))
# fig.show()  
#
#
