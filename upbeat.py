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
    print(unit)
    querystring = {"market": market, "count": count}
    print(url)
    print("------------")
    response = requests.request("GET", url, params=querystring)
    box = response.json()
    lst = []
    print(box)
    for i in box:
        temp = [i['market'],i['candle_date_time_kst'],i['opening_price'],i['high_price'],i['low_price'],i['trade_price'],i['candle_acc_trade_price'],i['candle_acc_trade_volume']]
        lst.append(temp)
        print(temp)
    df1 = pd.DataFrame(data = np.array(lst),columns=["코인명","캔들기준시간(KST 기준)","시가","고가","저가","중가","누적거래금액","누적거래량"])
    return lst

def getTradePriceDay(market,type,count):
    url = f"https://api.upbit.com/v1/candles/{type}/"

    querystring = {"market": market, "count": count}

    response = requests.request("GET", url, params=querystring)
    box = response.json()
    lst = []
    print(box)
    for i in box:
        temp = [i['market'],i['candle_date_time_kst'],i['opening_price'],i['high_price'],i['low_price'],i['trade_price'],i['candle_acc_trade_price'],i['candle_acc_trade_volume']]
        lst.append(temp)
        print(temp)
    df1 = pd.DataFrame(data = np.array(lst),columns=["코인명","캔들기준시간(KST 기준)","시가","고가","저가","중가","누적거래금액","누적거래량"])
    return lst
def getMarket():
    url = "https://api.upbit.com/v1/market/all"

    querystring = {"isDetails":"false"}

    response = requests.request("GET", url, params=querystring)
    box = response.json()
    lst = []
    
    for i in box:
        if("KRW"!=i['market'][:3]):
            continue
        temp = [i['korean_name'],i['market']]
        lst.append(temp)
    
    
    #df1 = pd.DataFrame(data = np.array(lst),columns=["코인명","코드"])
    #df1.to_csv("/Users/kimjungwoo/Downloads/coin_list.csv")  
    lst.sort()
    print(lst)
    return lst 
    
my_dict = getMarket()
getTradePriceDay(my_dict[0][1],"weeks",200)

