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



regex = re.compile(r'这么好')
br = mechanize.Browser()


# set cookie
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)



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

#cookie = 'U_TRS1=000000ad.12ea4540.55a6f1dc.a1f8515a; SINAGLOBAL=211.100.46.233_1437004252.461766; vjuids=-f7b4a6a52.14e9420cd4d.0.8524f673; SGUID=1437004255437_18452440; UOR=www.baidu.com,blog.sina.com.cn,; __utma=26655598.1826176666.1444445927.1444445927.1444445927.1; __utmz=26655598.1444445927.1.1.utmcsr=bdpp-xe-bj-20-wlb-lja-400|utmccn=(not%20set)|utmcmd=(not%20set)|utmctr=%E5%8C%97%E4%BA%AC%E4%BB%8A%E6%97%A5%E5%AE%B6%E5%9B%AD; Apache=221.223.241.23_1446382925.911956; ULV=1446383015869:73:4:4:221.223.241.23_1446382925.911956:1446382430577; U_TRS2=000000b7.63bb7910.56360ea5.c3b67494; lxlrtst=1446380538_o; SessionID=eip900nvffcmj0dih5oog06ec1; lxlrttp=1446380538; rotatecount=4; vjlast=1446368347.1446376622.10; ULOGIN_IMG=xd-1b43f50bbdf5aad75a3f9818105f4bd2f77e; cREMloginname=731840616%40qq.com; sso_info=v02m4a4vY2zjLGOg5CwjaOEtomTkLCcl4SumLa9rYmnlL2Jk4mCmaaVgpSjkaGQlYmvm4S9to2WtKWMpImVmbeRk5u2nKWMtJCljLSQppq3mL2MkMDA; SUB=_2AkMhapvddcNhrAZUkf0Uym_nZIlH-jjGiefBAH_tJWZ5HRgBSlex3jD10799fmViPyMVFd87sw..; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WWoOJiNgiKWY5YIkLJLzPGc'
#refer = 'http://login.sina.com.cn/signup/signin.php?entry=sso'

#cookie = 'SINAGLOBAL=6484463368542.492.1437097245826; __utma=15428400.1454781120.1447925140.1447925140.1447925140.1; __utmz=15428400.1447925140.1.1.utmcsr=zhidao.baidu.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; _s_tentry=login.sina.com.cn; Apache=8722460942808.539.1452565552930; ULV=1452565552949:115:3:1:8722460942808.539.1452565552930:1452255349903; NSC_wjq_txfjcp_mjotij=ffffffff094113d345525d5f4f58455e445a4a423660; myuid=5133209579; login_sid_t=6266bcd0187f743a785b6e7ba83df721; UOR=developer.51cto.com,widget.weibo.com,login.sina.com.cn; SUS=SID-5133209579-1452569104-XD-0pnvi-3548ef1f095cb4ff90ca9ea06f42271b; SUE=es%3Da95021745f5d6873554883581538478e%26ev%3Dv1%26es2%3Dcf1eeec6ed9a6894e42490d025a7bc0f%26rs0%3DZp%252BbMaQiLCH7iOSLum5UEoc8kBPZjhK%252FjD3FR7Ti7pbbr2B6gqBKt1Y5AxaKmJbflwf69xF9YCc8sSBJvMwE9Jt5jLdHDi8X8hrGNbXPvnzuVxQydIVO0q3TE1Tk1zwm7%252BL2HF44MM4WQPmhzUurPurdH5lG9I903IoqVMbzGek%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1452569104%26et%3D1452655504%26d%3Dc909%26i%3D271b%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D5133209579%26name%3D13522269132%26nick%3D%25E9%259D%2599%25E6%2580%259D975%26fmp%3D%26lcp%3D2015-10-17%252022%253A51%253A00; SUB=_2A257kAJADeRxGeNP6FET8CfJzDWIHXVY5HSIrDV8PUNbuNAPLVn2kW9LHeua-vZkPonz1bOK19JoFurFefteyA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWkqpgmwxf0-GeKzhfIh76r5JpX5K2t; SUHB=09PNLo_DWrVK2h; ALF=1484105104; SSOLoginState=1452569104; wvr=6; WBStore=5955be0e3d5411da|undefined'

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
#br.set_proxies({"https":"177.159.200.100:3128"})


# test post  stackoverflow  http://stackoverflow.com/questions/5035390/submit-without-the-use-of-a-submit-button-mechanize
# first step is get


t = str(int(time.time()*1000))
r = br.open('http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.15)&_=' +t)
html = r.read()
print html


html = html[html.index('preloginCallBack')+17:-1]
print html
d = json.loads(html)
print len(d)
nonce = d['nonce']
servertime = d['servertime']
rsakv = d['rsakv']
publickey = d['pubkey']
print nonce
print servertime
print rsakv
print publickey

passwd = ""
crawler = getRsa.Test()
sp = crawler.js(servertime, nonce.strip(), passwd, publickey)
print sp



t = str(int(time.time()*1000))
username = '13522269132'
su = base64.encodestring(username)
print su
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
print html
d = json.loads(html)
print len(d)
https = d['crossDomainUrlList']
print https

r = br.open(https[0])
print r.read()
r = br.open(https[1])
print r.read()
r = br.open(https[2])
print r.read()



t1 = str(int(time.time()))
t = str(int(time.time()*1000))
print t, t1
url = 'http://crosdom.weicaifu.com/sso/crosdom?action=login&savestate='+ t1 +'&callback=sinaSSOController.doCrossDomainCallBack&script\
Id=ssoscript1&client=ssologin.js(v1.4.15)&_=' + t + 'HTTP/1.1'
#host = 'crosdom.weicaifu.com'
#br.addheaders = [('Host', host)]

r = br.open(url)
print r.read()

r = br.open('http://login.sina.com.cn/')
print r.read()
r = br.open('http://login.sina.com.cn/member/app.php?entry=sso&act=my')
print r.read()
#r = br.open('http://s.weibo.com/weibo/data%2520science&page=9')
#html = r.read()
r = br.open('http://login.sina.com.cn/member/my.php?entry=sso')
#print r.read()
#print html

#r = br.open('http://weibo.com/u/5133209579/home?wvr=5')
#r = br.open('https://www.baidu.com/link?url=WGfYfteHfT7CkABTY3AboUc0x9sMWxrjBXOPHiyi4Pq&wd=&eqid=b09ad79f0000fe2e0000000256949e50')
#r = br.open('http://weibo.com/')
#print r.read()


r = br.open('http://s.weibo.com/weibo/data%2520science&page=9')
html = r.read()
#print html

r = br.open('http://weibo.com/p/1005051496959004/follow?relate=fans&page=3#Pl_Official_HisRelation__65')
html = r.read()
print html
#print type(cj)  
#f = open("dump.txt", 'wb')
#pickle.dump(cj, f)
#f.close()



'''
cook = ""
for ck in cj:
    cook = cook+ ck.name +"="+ck.value+";"
print cook
'''


#r = br.open('http://s.weibo.com/weibo/data%2520science&page=9')
#html = r.read()
#print html




'''
host='passport.weibo.com'
refer='http://login.sina.com.cn/signup/signin.php'
br.addheaders = [('Refer',refer),
        ('User-agent', user_agent),
        ('Host',host),
        ('Origin',origin),
        ('Content-Type',content_type),
        ('Connection', connection)
        #('Cookie', cookie)
        ]


r = br.open('http://wbsso/login?ticket=ST-NTEzMzIwOTU3OQ%3D%3D-1452576318-xd-9ABFEEFDECDEF4FFFA9B1ED09D46AE75&ssosavestate=1452576318&callback=sinaSSOController.doCrossDomainCallBack&scriptId=ssoscript0&client=ssologin.js(v1.4.15)&_=1452576317579 HTTP/1.1')
html = r.read()

r = br.open('http://s.weibo.com/weibo/data%2520science&page=9')
html = r.read()

print html
for ck in cj:
    print ck.name +":"+ck.value
'''
# test the request

#r = br.open('http://www.iqiyi.com')
#r = br.open('http://s.weibo.com/weibo/%25E5%25BC%25A0%25E4%25BA%25AE%25E9%25BA%25BB%25E8%25BE%25A3%25E7%2583%25AB&Refer=STopic_box')
#r = br.open('http://s.weibo.com/weibo/football&page=9')
#for i in range(0):
 #   print i
  #  time.sleep(2)
#r = br.open('http://s.weibo.com/weibo/%25E5%25BC%25A0%25E4%25BA%25AE%25E9%25BA%25BB%25E8%25BE%25A3%25E7%2583%25AB&b=1&page='+str(i+1))
#r =  br.open('http://s.weibo.com/weibo/%25E5%25BC%25A0%25E4%25BA%25AE%25E9%25BA%25BB%25E8%25BE%25A3%25E7%2583%25AB&b=1&page='+str(4))

#test weixin
#r = br.open('http://mp.weixin.qq.com/s?__biz=MzA5NTQyMzAxOQ==&mid=400013482&idx=1&sn=6dbf72db5451b45a3e0860c44b01be84&scene=0#rd')
#test the post

'''
for form in br.forms():
    if form.attrs['id'] ==
'''

'''
no = 0;

for i in range(50):
    time.sleep(random.randint(30,40))
    r = br.open('http://s.weibo.com/weibo/football&page='+str(i+1))
    html = r.read()
    print html
    judge =  html.find('你的行为有些异常')
    if judge > 0:
        break
    else:
        no += 1
print no
'''
#print html
#print regex.findall(html)
#print br.response().read()
#print br.title()
#print r.info()



