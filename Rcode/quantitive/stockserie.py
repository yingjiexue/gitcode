from pymongo import MongoClient
import tushare as ts
import numpy as np

def bound(data):
    data["year"]=data.index
    return data

client = MongoClient('localhost',27017)
db=client.Stock
collection=db.subcode
x=collection.find_one()


collection2=db.stockkdat
collection2.remove()

if type(x["code"])==str:
    stock = ts.get_k_data(x["code"])
    datastock = bound(stock)
    sdd = datastock.to_dict(orient='records')
    inf = {"id": x["code"], "stockbasic": sdd, }
    collection2.insert_one(inf)

else:
    for i in x['code']:
        stock=ts.get_k_data(i)
        if stock is None: continue
        datastock=bound(stock)
        sdd = datastock.to_dict(orient='records')
        inf = {"id": i, "stockbasic": sdd, }
        collection2.insert_one(inf)



client = MongoClient('localhost',27017)
db=client.Stock
collection=db.subcode
x=collection.find_one()
collection1=db.stockserie
collection1.remove()

if type(x["code"])==str:
    stock = ts.get_hist_data(x["code"])
    datastock = bound(stock)
    sdd = datastock.to_dict(orient='records')
    inf = {"id": x["code"], "stockbasic": sdd, }
    collection1.insert_one(inf)

else:
    for i in x['code']:
        stock=ts.get_hist_data(i)
        if stock is None: continue
        datastock=bound(stock)
        sdd = datastock.to_dict(orient='records')
        inf = {"id": i, "stockbasic": sdd, }
        collection1.insert_one(inf)


