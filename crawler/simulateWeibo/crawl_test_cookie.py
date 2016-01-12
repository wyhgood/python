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
cookie = 'LT=1452582658;tgc=TGT-NTEzMzIwOTU3OQ==-1452582658-xd-7D431D243D6D8DDA1D67A69A57431BF7;SRF=1452582658;SRT=E.vAfsJOJqJZvuiOVuv!PlAnmBvXvCvXMdb1VCvnmBBvzvvv4m534X4ARmvvvD0vVmP9QtXXXFvRvvvXLnCXzvYvrBJAtBvv0BvMmCvvzNvAzRvAv7*B.vAflW-P9Rc0lR-ykADvnJqiQVbiRVPBtS!r3JZPQVqbgVdWiMZ4siOzu4DbmKPWQT3EnS-s35FRnI4WbN39fS!bfiqSpi49ndDPIJeA7;SUB=_2A257kNdSDeRxGeNP6FET8CfJzDWIHXVY5E-arDV_PUJbuNAPLUL6kW9LHeuR-aCa9tkZZDJ3s5vMbrqA8Iq1ng..;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWkqpgmwxf0-GeKzhfIh76r;SUE=es%3D2d48656271d951e34fb7bf62598cbde1%26ev%3Dv1%26es2%3D22abacc42166c5e4811f4513528b8cf9%26rs0%3DDsiPjLSO0Idw8N0Mj%252Foyueg1476L%252FuidjPAenJUGAi10KKoICs6jjUMmis6L0%252Fv7aTv4bqDdXuI6KZhU05gcwH01Y%252FVU8tVXXCZ9bsEXxkXFEQTe3WUd7tAfta0q9ODEQXaHP4Hxs5SjOTML0wFFpajStLNJ6o%252BLBT7mEHJo30o%253D%26rv%3D0;SUP=cv%3D1%26bt%3D1452582658%26et%3D1452669058%26d%3D40c3%26i%3D38e2%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26lt%3D1%26uid%3D5133209579%26user%3D13522269132%26ag%3D1%26name%3D13522269132%26nick%3D%25E9%259D%2599%25E6%2580%259D975%26sex%3D%26ps%3D0%26email%3D%26dob%3D%26ln%3D13522269132%26os%3D%26fmp%3D%26lcp%3D2015-10-17%252022%253A51%253A00;SUS=SID-5133209579-1452582658-XD-n3xq5-cf4b295f86af4595cc2296e2bc7c38e2;sso_info=v02m6alo5qztKWRk6SljpSQpY6TpKWRk5iljoOApY6UkLmNs5SmnZalpI-TlLGMs4yyjIOktY2zpMA=;ALF=1455174658;SSOLoginState=1452582658;SSOLoginState=1452582658;SUB=_2A257kNdSDeRxGeNP6FET8CfJzDWIHXVY5E-arDV8PUJbuNAPLWX6kW9LHesczW6T_1wgyAisYsQ4teQyG5q8oQ..;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWkqpgmwxf0-GeKzhfIh76r5JpX5K2t;SUE=es%3D1fe2b70fd602c145ec3fa4ca742112c3%26ev%3Dv1%26es2%3D505a4e74dffbf7b5fffe2ab78c7d5ed1%26rs0%3DOVFmzHV9N0NzPPxfaD%252BkVHLYiXhdCAHc8cNar4MxSLW0i4q6UmdFs1eUwXK7WrEC%252BfwM0VPiy9fHsq70DALsFHbgajgOMelwllNcRlCUzb8YVUBnst929ntJLxEikb%252BU4%252FrnNea2x1e0SJb%252FOoLHeF2WycfmWdvp4lWBcT%252B%252Bzac%253D%26rv%3D0;SUHB=00xZai0BTivtpe;SUP=cv%3D1%26bt%3D1452582658%26et%3D1452669058%26d%3Dc909%26i%3D271b%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D5133209579%26name%3D13522269132%26nick%3D%25E9%259D%2599%25E6%2580%259D975%26fmp%3D%26lcp%3D2015-10-17%252022%253A51%253A00;SUS=SID-5133209579-1452582658-XD-r2768-3d774cd42a7991a1f0c665ce809e271b;wvr=6;ALF=1452582658;SSOLoginState=1452582659153;TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517;TC-V5-G0=c427b4f7dad4c026ba2b0431d93d839e;'

#cookie ='LT=1452581025;tgc=TGT-NTU5NTE2NDU4NA==-1452581025-xd-11AF36634AA7B3FF1845714AB85C1C49;SRF=1452581025;SRT=E.vAfsiO!sJORriOXrvcoOAnmBvXvCvXMdb1CYvnmBBvzvvv4m534X4ARmvvvD0vVmP9QpzAXFvRvvvXLnCXzvBvrBJAtBvv0BvMmCvvzNvAzRvAv7*B.vAflW-P9Rc0lR-ykADvnJqiQVbiRVPBtS!r3JZPQVqbgVdWiMZ4siOzu4DbmKPWQUry1T4ueT4kQdOPSNdkJN!ow4mWZi49ndDPIJeA7;SUB=_2A257kNDxDeTxGeNL4lcQ9irJwziIHXVY5EU5rDV_PUJbuNAPLWOkkW9LHesorLrsg9NSt6mge4TnRqom8op1BQ..;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWoOJiNgiKWY5YIkLJLzPGc;SUE=es%3Dac3c2d9f88c2eee25b372c58eae0ab18%26ev%3Dv1%26es2%3Db302f9cd80c61a2f7d2d60f8d72c3d23%26rs0%3DH4ITSfhbA0suZrrf6FpfZ6RquJAvGrLTa4J4c1vjp4BfMTorbHv%252BjbONFRAAKbmN7flyTkRwa0ViqtUgPRFLQEg6SHDbjyQVXfFKXzUj7%252BDcV8YBrmCARw53cpjxJY%252FYzRbfCteljqN%252FaAc5or4AQhGtgYceXtl5zkQEMS0xyCo%253D%26rv%3D0;SUP=cv%3D1%26bt%3D1452581025%26et%3D1452667425%26d%3D40c3%26i%3D38e2%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26lt%3D1%26uid%3D5595164584%26user%3D731840616%2540qq.com%26ag%3D4%26name%3D731840616%2540qq.com%26nick%3D%25E7%2594%25A8%25E6%2588%25B75595164584%26sex%3D%26ps%3D0%26email%3D%26dob%3D%26ln%3D731840616%2540qq.com%26os%3D%26fmp%3D%26lcp%3D;SUS=SID-5595164584-1452581025-XD-2runk-7a13b78dacf5ae05f8b0ec0fac5b38e2;sso_info=v02m6alo5qztKWRk5yljpOQpZCToKWRk5iljoOgpZCjnLWNk6S1jJOYtI2ToLSJp5WpmYO0tY2TpLWMk5i0jZOgtA==;ALF=1455173025;SSOLoginState=1452581025;SSOLoginState=1452581025;SUB=_2A257kNDxDeTxGeNL4lcQ9irJwziIHXVY5EU5rDV8PUJbuNAPLUzHkW9LHesFSSk9baIsqQPWD0VHW1RVuSYh_Q..;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWoOJiNgiKWY5YIkLJLzPGc5JpX5K2t;SUE=es%3Dba8ca86b191bba8fb76c0bfa29f7ddf9%26ev%3Dv1%26es2%3D1f785582a90b9ed5b5bb5ba4489032fc%26rs0%3D0bcnBE2WjD7G%252BAqxqxDUBquNj8JVXMYHkcrbv05RNJ0jeYF%252FqWdcV7gZ0b0dNZgZwFKBnYyD0h73L037Q8FtBGHvUZ4OaRGtKMVvg%252FWd4K49fZYYl%252FrN2uF%252BN9DAi%252Ft25sO1HyzYZf1%252Flx5EK%252FrUfFWrzjTmc24w%252Fn%252BkZP2pL7c%253D%26rv%3D0;SUHB=00x5P8SffivvRg;SUP=cv%3D1%26bt%3D1452581025%26et%3D1452667425%26d%3Dc909%26i%3D271b%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D5595164584%26name%3D731840616%2540qq.com%26nick%3D%25E7%2594%25A8%25E6%2588%25B75595164584%26fmp%3D%26lcp%3D;SUS=SID-5595164584-1452581025-XD-9hgk7-4ba9be523e385b39a46803df1b9a271b;ALF=1452581025;SSOLoginState=1452581025720;miaopai=usrmdinst_1;TC-Page-G0=4e714161a27175839f5a8e7411c8b98c;TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517;'

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
        ('Connection', connection),
        ('Cookie', cookie)
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

passwd = "pxfg73uv"
crawler = getRsa.Test()
sp = crawler.js(servertime, nonce.strip(), passwd, publickey)
print sp



t = str(int(time.time()*1000))
username = '731840616@qq.com'
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
#r = br.open(post_url, data)
#html = r.read()
r = br.open('http://s.weibo.com/weibo/data%2520science&page=9')
html = r.read()
print html
for ck in cj:
    print ck.name +":"+ck.value

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



