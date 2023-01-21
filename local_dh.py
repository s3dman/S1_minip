import pickle
import os

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
    db = ReadDB("DATABASE.DB")['symbols']
    return db