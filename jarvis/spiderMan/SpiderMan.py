import urllib.request

#要伪装成的浏览器(我这个是用的chrome)
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36')
url='http://www.oschina.net'
opener = urllib.request.build_opener()
#将要伪装成的浏览器添加到对应的http头部
opener.addheaders=[headers]
#读取相应的url
data = opener.open(url).read()
#将获得的html解码为utf-8
data=data.decode('utf-8')
print(data)