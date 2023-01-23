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

def userDataStore(user,data):
    db = ReadDB("USERDATA.DB")
    db[user] = data
    WriteDB(db,"USERDATA.DB")

# v = {}
# def data_storer():
#     for i in "MSFT AAPL".split():
#         global v
#         ticker = yfinance.Ticker(i)
#         x = dict(ticker.info)
#         # x["Name"] = SymbolGet()[i]
#         v[i] = x
