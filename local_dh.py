import pickle
import yfinance

# to write a data object to a file
def WriteDB(db,file):
    with open(f'./database/{file}','wb') as db_file:
        pickle.dump(db,db_file)

# to read a stored data object from a file
def ReadDB(file):
    with open(f'./database/{file}','rb') as db_file:
        db = pickle.load(db_file)
    return db

def initialize():
    db = {'users':{}}
    WriteDB(db,"DATABASE.DB")

def SymbolGet():
    db = ReadDB("STOCKLIST.DB")
    return db

def initialization_download():
    s = ""
    for i in SymbolGet():
        s += f"{i} "
    s = s.strip()
    data = yfinance.download(tickers=s,period='max',interval='1d',repair=True)
    x = {}
    dates = [j.timestamp() for j in list(data.index)]
    for i in SymbolGet():
        x[i] =  dates,list(data["Open"][i]),list(data["High"][i]),list(data["Low"][i]),list(data["Close"][i])
    WriteDB(x,"STOCKDATA.DB")