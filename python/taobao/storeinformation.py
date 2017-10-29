from test import *
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db=client.TMstoreinf
collection=db.TMstoreinf
try:
    login("用户名","密码")
finally:
    time.sleep(10)
    product_name("要搜索的产品名字")
    time.sleep(10)
    for  j in range(0,70):
        n=0
        m=0
        while n<60:
            whichprodut(n)
            time.sleep(5)
            try:
                g=generalinf()
                s=storeinf()
                id =g+s
                inf={"_id":g[1:100],"ginf":g,"sinf":s}
                n=n+1
            except:
                browser.close()
                print("页面错误")
                s2 = browser.window_handles
                browser.switch_to_window(s2[0])
                continue
            try:
                collection.insert_one(inf)
            except:
                print("id is identical")
            finally:
                s1 = browser.window_handles
                browser.switch_to_window(s1[1])
                browser.close()
                browser.switch_to_window(s1[0])
                print("第" + str(j + 1) + "页," + "第" + str(n + 1) + "商品")
        page()
