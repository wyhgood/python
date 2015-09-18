#!/usr/bin/python
import sys, mechanize
print 1

br = mechanize.Browser()

br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

#Follows refesh
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)

#user-agent 
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.set_proxies({"http":""})


r = br.open('http://www.baidu.com')
html = r.read()
print html
print br.response().read()
print br.title()
print r.info()

