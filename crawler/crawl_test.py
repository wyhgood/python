#!/usr/bin/python
#coding=utf-8
import sys, mechanize
import urllib
import cookielib
import re
import time
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

#cookie = 'SINAGLOBAL=6484463368542.492.1437097245826; TC-Ugrow-G0=968b70b7bcdc28ac97c8130dd353b55e; login_sid_t=1742def9a042d5b25c356c27ae3d1639; _s_tentry=passport.weibo.com; Apache=334385652095.0794.1445094195932; ULV=1445094195944:59:18:12:334385652095.0794.1445094195932:1445093408259; TC-V5-G0=7e5b74ea4beaaa98b5f592db11c2eeb9; TC-Page-G0=9183dd4bc08eff0c7e422b0d2f4eeaec; myuid=5133209579; UOR=developer.51cto.com,widget.weibo.com,login.sina.com.cn; SUS=SID-5133209579-1445096505-XD-wb0yj-6bac97334a3131da5ad393da71a1226c; SUE=es%3D9cf8a4d729bbbc5ff8b89408ef778990%26ev%3Dv1%26es2%3D73cc67e3150b0b739573d8a9b51125bb%26rs0%3Dvh%252Bwa%252FFbfVgHpaxuDLSAyGeP1fUmxzlMD9EVflfekDq71SmwlzNOyYGhREFApEz4OSy3%252BaL8QjptWkgzuP3DHX%252Bg%252B%252F7V%252Bod95IbtrEoqc1jHS6c632zF1kDbC8f1uLQnQZW7Gq3hmx8mKyEf1%252BD4qKt6t4Jx0lw%252FaSWX6r%252BlAsI%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1445096505%26et%3D1445182905%26d%3Dc909%26i%3D226c%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D5133209579%26name%3D13522269132%26nick%3D%25E9%259D%2599%25E6%2580%259D975%26fmp%3D%26lcp%3D2015-10-17%252022%253A51%253A00; SUB=_2A257JhxpDeTxGeNP6FET8CfJzDWIHXVYUgqhrDV8PUJbuNAPLVelkW-WoQLuaLVFJsAoTtk_6CCJJqwC8w..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWkqpgmwxf0-GeKzhfIh76r5JpX5K2t; SUHB=0u5hWNwmXSiXsE; SSOLoginState=1445096505; un=13522269132; wvr=6'
cookie = 'SINAGLOBAL=6484463368542.492.1437097245826; un=13522269132; NSC_wjq_txfjcp_mjotij=ffffffff094113da45525d5f4f58455e445a4a423660; _s_tentry=-; Apache=535806191619.4856.1445097081288; ULV=1445097081303:60:19:13:535806191619.4856.1445097081288:1445094195944; un=13522269132; myuid=5133209579; WBStore=4e40f953589b7b00|undefined; WBtopGlobal_register_version=cde4e46930babd9e; crossidccode=CODE-xd-1zNurX-3kJ2ZB-qvljCYQvqfxLfnW09042c; SSOLoginState=1445099720; SUS=SID-5510913203-1445099720-XD-j8917-ada2416a4c20c258d69db98f2f8edd3d; SUE=es%3D16014741b2fb6b84fc3ecf04dea80e1f%26ev%3Dv1%26es2%3D77c346191c21996fe21722b367c6afc7%26rs0%3DjTbEQ5tAYJAYj1XO35XbmNVkghhOq2sx1wmen867LKCE44YQ5tm31gCq9fUkY6Va9hAuyiwPdBWRdDG3mXXecPVUVvn%252Bxj1fO0s6lrqS1mM6IeKdY4Nwwv0P84NeMBiLM32VhsuvSdfDoGkko5%252BVOlA5Gsqnqjfi3fVx%252FrxErvs%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1445099720%26et%3D1445186120%26d%3Dc909%26i%3Ddd3d%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D5510913203%26name%3D%26nick%3D%25E5%2585%25B6%25E5%25AE%259E%25E6%2588%2591%25E6%2598%25AF%25E6%2596%2587%25E7%25A7%2591%25E7%2594%259F%25E4%25BA%2586%26fmp%3D%26lcp%3D; SUB=_2A257JgiYDeTxGeNL6lIY8S3Oyz-IHXVYUn1QrDV8PUNbu9APLWjnkW9RffAXyB5Bv4KEKyXMr3oqBOrbjw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW43nLxN54m28.8Vk6Zs7605JpX5Kzt; SUHB=0HTxK0rfOV98Jd; ALF=1476635719; UOR=developer.51cto.com,widget.weibo.com,login.sina.com.cn'
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615Fedora/3.0.1-1.fc9 Firefox/3.0.1'),('Host','www.weibo.com'),('cookie',cookie)]



#set proxy
br.set_proxies({"http":"123.103.8.218:80"})




# test the request

#r = br.open('http://www.iqiyi.com')
#r = br.open('http://s.weibo.com/weibo/%25E5%25BC%25A0%25E4%25BA%25AE%25E9%25BA%25BB%25E8%25BE%25A3%25E7%2583%25AB&Refer=STopic_box')
#r = br.open('http://weibo.com')
#for i in range(0):
 #   print i
  #  time.sleep(2)
#r = br.open('http://s.weibo.com/weibo/%25E5%25BC%25A0%25E4%25BA%25AE%25E9%25BA%25BB%25E8%25BE%25A3%25E7%2583%25AB&b=1&page='+str(i+1))
r =  br.open('http://s.weibo.com/weibo/%25E5%25BC%25A0%25E4%25BA%25AE%25E9%25BA%25BB%25E8%25BE%25A3%25E7%2583%25AB&b=1&page='+str(4))

#test the post

'''
for form in br.forms():
    if form.attrs['id'] ==
'''



html = r.read()
print html
#print regex.findall(html)
print br.response().read()
#print br.title()
#print r.info()


