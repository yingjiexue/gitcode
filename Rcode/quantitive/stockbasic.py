import multiprocessing

import tushare as ts

import pandas as pd

from pymongo import MongoClient

z=ts.get_stock_basics()

client = MongoClient('localhost', 27017)

db = client.Stock

collection1=db.code

collection1.remove()

id=z.index

name=z['name']

x={'code':id,'name':name}

ys=pd.DataFrame(data=x)

inf=ys.to_dict(orient='records')

ks = {"_id": "stockcode", "stockcod": inf, }

collection1.insert_one(ks)


collection = db.basic

collection.remove()


for i in range(0, len(z.index)):
    x = z.iloc[i].to_dict()

    x['timeToMarket'] = str(x['timeToMarket'])

    inf = {"id": z.index[i], "stockbasic": x, }

    collection.insert_one(inf)


