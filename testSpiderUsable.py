# -*- coding: UTF-8 -*-
import re
import conf
import urllib2



headers = {
	    "cookie": conf.cookies
	}

url="https://weibo.com/130189890"


request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
html = response.read()

print(html)


