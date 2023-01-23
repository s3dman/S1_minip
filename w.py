import pandas as pd
import json
import requests



def get_exchange_data(key,exchange='NASDAQ'):
    """
    returns metadata for a specific exchange

    """
    endpoint = f"https://eodhistoricaldata.com/api/exchange-symbol-list/"
    endpoint += f"{exchange}?api_token={key}&fmt=json"
    print("Downloading data")
    call=requests.get(endpoint).text
    exchange_data=pd.DataFrame(json.loads(call))
    print("Completed")
    return exchange_data

def main():
    key = "63ccde6cea9b50.93764423"
    a=get_exchange_data(key)
    a.to_csv('indexesss2.csv')


if __name__ ==  '__main__':
    main()

