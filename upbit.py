import hashlib
import time
from urllib.parse import urlencode
import jwt
import requests
import uuid
import pandas as pd
import numpy as np
from key import S_KEY,A_KEY


SECRET_KEY = S_KEY
ACCESS_KEY = A_KEY


def getTradePrice(market, count, type,unit):
    url = f"https://api.upbit.com/v1/candles/{type}/{unit}"
    querystring = {"market": market, "count": count}
    response = requests.request("GET", url, params=querystring)
    box = response.json()
    lst = []
    for i in box:
        temp = [i['market'],i['candle_date_time_kst'],i['opening_price'],i['high_price'],i['low_price'],i['trade_price'],i['candle_acc_trade_price'],i['candle_acc_trade_volume']]
        lst.append(temp)
        print(temp)
    return lst

def getTradePriceDay(market,type,count):
    url = f"https://api.upbit.com/v1/candles/{type}/"

    querystring = {"market": market, "count": count}

    response = requests.request("GET", url, params=querystring)
    box = response.json()
    lst = []
    for i in box:
        temp = [i['market'],i['candle_date_time_kst'],i['opening_price'],i['high_price'],i['low_price'],i['trade_price'],i['candle_acc_trade_price'],i['candle_acc_trade_volume']]
        lst.append(temp) 
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
    lst.sort()
    return lst 
    

