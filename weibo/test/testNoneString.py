#coding:utf8
'''
Created on 2016年4月21日

@author: wb-zhaohaibo
'''
import re
import time

tt1 = time.time()
ss = ""
if ss == "":
    print "tyee"
else:
    print "ss"


s1 = "dasddfghasd"
aa = s1.find("asgg")
print aa


data = {}
if data is None:
    print "None"
else:
    print "not None "

if len(data) != 0:
    print "not 0"
else:
    print "0"


nickName = "lemon柠檬-L~。。。".decode("utf8")
patten = re.compile(ur'([\u4e00-\u9fa5\w_\-~]+)')
s = patten.findall(nickName)
print s[0]

tt2 = time.time()

tt = tt2 - tt1
print "耗时 %d" % tt

count = 5000
print count % 3000


# list = [1,2,3]
# if 4 in list:
#     print "true11"
# else:
#     print "false00"

