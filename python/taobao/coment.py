from test import *
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient('localhost',27017)
db=client.Comment
collection=db.Comment
try:
    login("用户名","密码")
    time.sleep(7)
finally:
    product_name("搜索的产品名")
    time.sleep(6)
for  j in range(70,73):
    page(j)
    n=0
    while n<60:
        whichprodut(n)
        time.sleep(2)
        n = n + 1
        try:
            g=generalinf()
            f=collection.find_one({'_id':g[1:100]})
            if f==None:
                x = comment()
                inf = {"_id": g[1:100], "coment": x, }
                collection.insert_one(inf)
            else:
                browser.close()
                print("id is identical")
                continue
        except:
            browser.close()
            print("页面错误")
            n=n-1
            s2 = browser.window_handles
            browser.switch_to_window(s2[0])
            continue
        finally:
            s1 = browser.window_handles
            browser.switch_to_window(s1[0])
            print("第" + str(j ) + "页," + "第" + str(n) + "商品")

