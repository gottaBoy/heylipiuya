import urllib2

req = urllib2.Request('http://www.baidu.com')
res = urllib2.urlopen(req)
print res.code
print res.read()
res.close()