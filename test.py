import top.api

req = top.api.TbkItemGetRequest()
req.set_app_info(top.appinfo(24533259, "58e00610ceeaafed2d8ba7ab59c2d3ac"))

req.fields = "num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick"
req.q = "女装"
#req.cat = "16,18"
#req.itemloc = "杭州"
# req.sort = "tk_rate_des"
# req.is_tmall = "false"
# req.is_overseas = "false"
# req.start_price = 10
# req.end_price = 10
# req.start_tk_rate = 123
# req.end_tk_rate = 123
# req.platform = 1
# req.page_no = 1
# req.page_size = 20
resp = req.getResponse()
print(resp)
# try:
#     resp = req.getResponse()
#     print(resp)
# except Exception as e:
#     print(e)