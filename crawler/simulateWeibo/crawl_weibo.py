#!/usr/bin/python
#coding=utf-8
import sys, mechanize
import urllib
import cookielib
import re
import time
import random
import json
import base64
import getRsa
import pickle

reload(sys)
sys.setdefaultencoding('utf-8')


def getBr(usr, pwd):

  br = mechanize.Browser()
  # set cookie
  cj = cookielib.LWPCookieJar()
  br.set_cookiejar(cj)
  #set configure
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
  refer = 'http://login.sina.com.cn/?r=%2Fmember%2Fmy.php%3Fentry%3Dsso'
  host = 'login.sina.com.cn'
  origin = 'http://login.sina.com.cn'
  content_type = 'application/x-www-form-urlencoded'
  user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'
  connection = 'keep-alive'
  br.addheaders = [('Refer',refer),
          ('User-agent', user_agent),
          ('Host',host),
          ('Origin',origin),
          ('Content-Type',content_type),
          ('Connection', connection)
          #('Cookie', cookie)
          ]

  #set proxy
  br.set_proxies({"http":"85.143.164.100:81"})


  # test post  stackoverflow  http://stackoverflow.com/questions/5035390/submit-without-the-use-of-a-submit-button-mechanize
  # first step is get --- prelogin
  t = str(int(time.time()*1000))
  r = br.open('http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.15)&_=' +t)
  html = r.read()
  #print html
  # get the para from prelogin response
  html = html[html.index('preloginCallBack')+17:-1]
  #print html
  d = json.loads(html)
  #print len(d)
  nonce = d['nonce']
  servertime = d['servertime']
  rsakv = d['rsakv']
  publickey = d['pubkey']
  #print nonce
  #print servertime
  #print rsakv
  #print publickey
  username = usr
  passwd = pwd

  #call js code 
  crawler = getRsa.Test()
  sp = crawler.js(servertime, nonce.strip(), passwd, publickey)

  t = str(int(time.time()*1000))
  su = base64.encodestring(username)
  #print su
  #su = 'MTM1MjIyNjkxMzI='
  post_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)&_='+t
  #post_url = '/sso/login.php?client=ssologin.js(v1.4.15)&_='+t+' HTTP/1.1'
  params = {
          'entry':'sso',
          'gateway':'1',
          'from':'null',
          'savestate':'0',
          'useticket':'0',
          'pagerefer':'',
          'vsnf':'1',
          'su': su,
          'service':'sso',
          'servertime':servertime,
          'nonce':nonce,
          'pwencode':'rsa2',
          'rsakv':rsakv,
          'sp':sp,
          'sr':'1366*768',
          'encoding':'UTF-8',
          'cdult':'3',
          'domain':'sina.com.cn',
          'prelt':'0',
          'returntype':'TEXT'
          }
  data = urllib.urlencode(params)
  r = br.open(post_url, data)
  html = r.read()
  #print html
  d = json.loads(html)
  #print len(d)
  https = d['crossDomainUrlList']
  #print https
  # requeset three url from the response 
  r = br.open(https[0])
  #print r.read()
  r = br.open(https[1])
  #print r.read()
  r = br.open(https[2])
  #print r.read()


  t1 = str(int(time.time()))
  t = str(int(time.time()*1000))
  #print t, t1
  url = 'http://crosdom.weicaifu.com/sso/crosdom?action=login&savestate='+ t1 +'&callback=sinaSSOController.doCrossDomainCallBack&scriptId=ssoscript1&client=ssologin.js(v1.4.15)&_=' + t + 'HTTP/1.1'
  #host = 'crosdom.weicaifu.com'
  #br.addheaders = [('Host', host)]

  r = br.open(url)
  #print r.read()

  r = br.open('http://login.sina.com.cn/')
  print r.read()
  r = br.open('http://login.sina.com.cn/member/app.php?entry=sso&act=my')
  print r.read()
  #r = br.open('http://s.weibo.com/weibo/data%2520science&page=9')
  #html = r.read()
  r = br.open('http://login.sina.com.cn/member/my.php?entry=sso')
  
  #test islogin
  r = br.open('http://s.weibo.com/weibo/data%2520science&page=9')
  html = r.read()
  
  #print html

    #f = open("dump.txt", 'wb')
  #pickle.dump(cj, f)
  #f.close()
  return br
if __name__ == '__main__':
    usr = '13522269132'
    pwd = 'pxfg73uv'
    url = 'http://s.weibo.com/weibo/data&page=27'
    br = getBr(usr, pwd);
    r = br.open(url)
    print r.read()
    print usr

