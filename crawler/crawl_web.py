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


br = mechanize.Browser()
r = br.open('http://www.66rere.com/se/dushijiqing/index_2.html')
html = r.read()
print(html)



