from urllib import request

type="www_quan"
appkey="878aqnxvux"
page=1
url="http://api.dataoke.com/index.php?r=goodsLink/www&type=www_quan&appkey=878aqnxvux&v=2&page=1"
info=request.Request(url)
infodata=request.urlopen(info).read()
print(infodata)