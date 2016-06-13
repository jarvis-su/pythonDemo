
import urllib.parse
o = urllib.parse.urlparse('http://www.smzdm.com/p/6076577/')
print(o)
print(o.path)
print(o.scheme)
print(o.port)
print(o.geturl())
