#coding:utf8
'''
Created on 2016年4月19日

@author: wb-zhaohaibo
'''
#下载微博主页页面信息
from bs4 import BeautifulSoup

from distutils.sysconfig import get_python_lib
import MySQLdb
html_cont = open("user.html","r").read()
soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
tags = soup.findAll("script")
if len(tags) > 1:
    #获取包含微博内容的script
    tag = tags[len(tags)-2].get_text()
#     print tag
    indexBegin = tag.index("<div")
    indexEnd = tag.rindex("<\/div>")
    contStr = tag[indexBegin:indexEnd+7]
    contStr = contStr[0:100]
    print contStr
    contStr = contStr.replace('\\"','"')
    contStr = contStr.replace('\\r','"')
    print contStr
    
    print get_python_lib()
    print MySQLdb