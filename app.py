from flask import Flask, render_template, request,Response ,url_for,send_file
from upbit import getMarket,getTradePriceDay,getTradePrice
from io import StringIO
import pandas as pd
import numpy as np


app = Flask(__name__)

@app.route("/")
def hello():
    my_list = getMarket()
    return render_template("index.html",market_list = my_list,ver = "55")

@app.route('/chart',methods=['GET','POST'])
def get_chart():
    
    if request.method == 'POST':
        pass
    elif request.method == 'GET':

        coin = request.args.get('coin')
        type = request.args.get('type')
        count = request.args.get('count')
        unit = request.args.get('unit')
        market_list = getMarket()
        for i in market_list:
            if(i[1]==coin):
                coin_name = i[0]

        if(type=="minutes"):
            list = getTradePrice(coin,count,type,unit)
        else:
            list = getTradePriceDay(coin,type,count)
        print(unit)
        return render_template('index.html',list = list ,market_list = market_list,coin_name = coin_name,unit=unit,type=type,count=count,coin=coin,ver = "55")



@app.route('/export')
def export():
    coin = request.args.get('coin')
    type = request.args.get('type')
    count = request.args.get('count')
    unit = request.args.get('unit')
    market_list = getMarket()
    print(unit)
    for i in market_list:
        if(i[1]==coin):
            coin_name = i[0]
    
        
    if(type=="minutes"):
        list = getTradePrice(coin,count,type,unit)
    else:
        list = getTradePriceDay(coin,type,count)
    for i in list:
        i[0] = coin_name
    df1 = pd.DataFrame(data = np.array(list),columns=["코인명","캔들기준시간(KST 기준)","시가","고가","저가","중가","누적거래금액","누적거래량"])  
    df1.to_csv(f"{coin}.csv", mode='w')


    if(type=="minutes"):
        return send_file(
            f"{coin}.csv",
            mimetype='text/csv',
            attachment_filename=f'{coin_name}_{unit}minutes.csv',
            as_attachment=True)
    else:
        return send_file(
            f"{coin}.csv",
            mimetype='text/csv',
            attachment_filename=f'{coin_name}_{type}.csv',
            as_attachment=True)      
if __name__ == '__main__':
    app.run(debug=True)