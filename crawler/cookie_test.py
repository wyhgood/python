#!/usr/bin/python
'''

test the cookie lib
'''

import urllib2
import cookielib



cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
opener.open('http://www.baidu.com')

print cookie
for ck in cookie:
    print ck.name,':',ck.value
