#!/usr/bin/python
#coding=utf-8
import sys, mechanize
import urllib
import cookielib
import re
import time
import random
import json
import rsa
import base64

reload(sys)
sys.setdefaultencoding('utf-8')

print 1

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

#cookie = 'SINAGLOBAL=6484463368542.492.1437097245826; un=13522269132; un=13522269132; myuid=5133209579; SUS=SID-5510913203-1445267363-XD-0gdol-71db387c954507f69c2b9e03d5787a9b; SUE=es%3Dd8a720fe976d927322694eadc06b8140%26ev%3Dv1%26es2%3D3fa4794fa49fcb839ae871fc335c17fc%26rs0%3DYH%252F0BZ7Zztqcb1NCUCqy6vrSWfN72RyhZfKSHpzzKNmbil1lfE39JtSWzcYqqTxc7gT%252BFTvmD6bAfhIfWqf4qj54JU%252FlptvrBm%252F1Dk5eh%252FVAhTbXI5i0uR5aFbrH1CIYTXrOreVMdNMedUL15MZFQVw5w%252B8PrFLw6Yei%252BpI0RYA%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1445267363%26et%3D1445353763%26d%3Dc909%26i%3D7a9b%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D5510913203%26name%3D%26nick%3D%25E5%2585%25B6%25E5%25AE%259E%25E6%2588%2591%25E6%2598%25AF%25E6%2596%2587%25E7%25A7%2591%25E7%2594%259F%25E4%25BA%2586%26fmp%3D%26lcp%3D; SUB=_2A257IXfzDeTxGeNL6lIY8S3Oyz-IHXVYV-47rDV8PUNbvtAPLVDRkW98Jan7uLH1X5r6YR31DafN_vuaBw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW43nLxN54m28.8Vk6Zs7605JpX5KMt; SUHB=0eb9N4ij1F-NYN; ALF=1476803362; SSOLoginState=1445267363; _s_tentry=login.sina.com.cn; UOR=developer.51cto.com,widget.weibo.com,login.sina.com.cn; Apache=262189193163.0671.1445267368670; ULV=1445267368739:63:22:3:262189193163.0671.1445267368670:1445222879002; NSC_wjq_txfjcp_mjotij=ffffffff094113d445525d5f4f58455e445a4a423660; WBStore=4e40f953589b7b00|undefined'
#cookie = ''

refer = 'http://login.sina.com.cn/signup/signin.php?entry=sso'
host = 'login.sina.com.cn'
origin = 'http://login.sina.com.cn'
content_type = 'application/x-www-form-urlencoded'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'

br.addheaders = [('Refer',refer),
        ('User-agent', user_agent),
        ('Host',host),
        ('Origin',origin),
        ('Content-Type',content_type)
        ]



#set proxy
#br.set_proxies({"http":"103.53.16.6:8080"})


# test post  stackoverflow  http://stackoverflow.com/questions/5035390/submit-without-the-use-of-a-submit-button-mechanize
# first step is get

t = str(int(time.time()*1000))
r = br.open('http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.15)&_=' +t)
html = r.read()
print html
#html = '{"retcode":0,"servertime":1445687742,"pcid":"xd-b6659b2599772a0df41e8f52aa650b23a78f","nonce":"IH8Z7P","pubkey":"EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443","rsakv":"1330428213","exectime":9})'



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

n = int(publickey, 16)
password = 'pxfg73uv'
pubkey = rsa.PublicKey(n, 10001)
pub = pubkey.save_pkcs1()
pubfile = open('public.pem','w+')
pubfile.write(pub)
pubfile.close()

message = str(servertime) +"\t"+ nonce + "\n" + password
print message

#message = "123"

with open('public.pem') as publickfile:
    p = publickfile.read()
    print p
    pubkey = rsa.PublicKey.load_pkcs1(p)

message = message.encode('utf-8').strip()
sp = rsa.encrypt(message, pubkey)
print sp



t = str(int(time.time()*1000))
username = '13522269132'
su = base64.encodestring(username)
print su
post_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)&_='+t
params = {'entry':'sso',
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



