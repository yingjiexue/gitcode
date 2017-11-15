#-*——coding utf-8 -*-
#导入模块
from test import *
from pymongo import MongoClient                               #导入mongo数据库模块
client = MongoClient('localhost',27017)                       #打开数据库
db=client.Comment                                             #创建数据库名
collection=db.Comment                                         #创建table
try:
    login("用户名","密码")                                    #登陆天猫国际
    time.sleep(7)
finally:
    product_name("搜索的产品名")                              #搜索产品
    time.sleep(6)
for  j in range(0,73):                                       #遍历所有页面
    page(j)
    n=0
    while n<60:                                              #遍历页面中的商品
        whichprodut(n)
        time.sleep(2)
        n = n + 1
        try:
            g=generalinf()                                   #获取店铺商品信息
            f=collection.find_one({'_id':g[1:100]})          #从数据库查找该商品信息
            if f==None:
                x = comment()                                #抓取客户对商品的评论
                inf = {"_id": g[1:100], "coment": x, }
                collection.insert_one(inf)                   #存入数据库中
            else:
                browser.close()
                print("id is identical")
                continue
        except:
            browser.close()
            print("页面错误")
            n=n-1                                             #如果抓取或存入出现错误关闭页面重新爬去
            s2 = browser.window_handles
            browser.switch_to_window(s2[0])
            continue
        finally:
            s1 = browser.window_handles
            browser.switch_to_window(s1[0])                     #抓取结束打印商品的页码和商品id
            print("第" + str(j ) + "页," + "第" + str(n) + "商品")

