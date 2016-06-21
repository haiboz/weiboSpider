#encoding:utf8
'''
Created on 2016年4月12日

@author: wb-zhaohaibo
'''
import spynner

browser = spynner.Browser()
browser.load("http://papers.cnki.net/shipeijun56")
html = browser.html.encode("utf-8")
print html