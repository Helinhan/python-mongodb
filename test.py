import top.api
from pymongo import *


'''
链接数据库
'''
def insert():
    try:
        client=MongoClient(host="localhost",port=27017)# 创建连接对象
        db=client.goods#获取数据库
        return db
    except Exception as e:
        print(e)


req = top.api.TbkUatmFavoritesGetRequest()
req.set_app_info(top.appinfo(24533259,"58e00610ceeaafed2d8ba7ab59c2d3ac"))

req.page_no = 1
req.page_size = 20
req.fields = "favorites_title,favorites_id,type"
req.type = 1
try:
    resp = req.getResponse()
    print(resp)
except Exception as e:
    print(e)
