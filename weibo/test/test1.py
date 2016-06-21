#encoding:utf-8
'''
Created on 2016年4月11日

@author: wb-zhaohaibo
'''
    
from bs4 import BeautifulSoup
import urllib2  
import re  
import string  
import sys  
import codecs  
  
url = r"http://www.weather.com.cn/weather/101070105.shtml"  
  
lookutf_8 = codecs.lookup('utf8')  
  
resContent = urllib2.urlopen(url).read()  
  
resContent = lookutf_8.decode(resContent)[0]  
resContent = lookutf_8.encode(resContent)[0]  
  
soup = BeautifulSoup(resContent)  
  
  
weatherYuBao = soup.findAll('div',id='7d')  
print weatherYuBao  
  
url = r"http://www.weather.com.cn/weather/101010100.shtml?"  
  
resContent = urllib2.urlopen(url).read()  
  
resContent = lookutf_8.decode(resContent)[0]  
resContent = lookutf_8.encode(resContent)[0]  
  
soup =BeautifulSoup(resContent)  
  
weatherYuBao = soup.findAll('div',id='7d')  
print weatherYuBao  


