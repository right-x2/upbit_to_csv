import hashlib
import time
from urllib.parse import urlencode
import jwt
import requests
import uuid
import pandas as pd
import numpy as np

SECRET_KEY = 'M7sMrk75HG2MGjO6nGSvT5jXAcx5RxBeJxM5SAwp'
ACCESS_KEY = 'PvKNRZ8Sy4StgXlxzPI4u2qZTbgxxQ205kD42KxC'


def getTradePrice(market, count, type,unit):
    url = f"https://api.upbit.com/v1/candles/{type}/{unit}"

    querystring = {"market": market, "count": count}

    response = requests.request("GET", url, params=querystring)
    print(response.json()[0]['candle_date_time_kst'])
    box = response.json()
    for i in box:
        print(i['candle_date_time_utc'])
    print(response.json())

def getTradePriceDay(market,count):
    url = f"https://api.upbit.com/v1/candles/days/"

    querystring = {"market": market, "count": count}

    response = requests.request("GET", url, params=querystring)
    box = response.json()
    lst = []
    for i in box:
        temp = [i['market'],i['candle_date_time_kst'],i['opening_price'],i['high_price'],i['low_price'],i['trade_price'],i['candle_acc_trade_price'],i['candle_acc_trade_volume']]
        lst.append(temp)
        print(temp)
    df1 = pd.DataFrame(data = np.array(lst),columns=["코인명","캔들기준시간(KST 기준)","시가","고가","저가","중가","누적거래금액","누적거래량"])
    df1.to_csv("/Users/kimjungwoo/Downloads/coin_list.csv")  
def getMarket():
    url = "https://api.upbit.com/v1/market/all"

    querystring = {"isDetails":"false"}

    response = requests.request("GET", url, params=querystring)
    box = response.json()
    my_dict = {}

    
    for i in box:
        my_dict[i['korean_name']] = i['market']
    
    
    #df1 = pd.DataFrame(data = np.array(lst),columns=["코인명","코드"])
    #df1.to_csv("/Users/kimjungwoo/Downloads/coin_list.csv")  
    return my_dict  
    
my_dict = getMarket()
getTradePriceDay(my_dict["도지코인"],200)

