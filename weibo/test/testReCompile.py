#encoding:utf8
'''
Created on 2016年4月12日

@author: wb-zhaohaibo
'''
import re
from bs4 import BeautifulSoup
html_cont = open("text.html","r").read()
soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
# sss = "/u/5888088457?refer_flag=1005050008_"
# pattern = re.compile(r"/u/[0-9]+\?refer_flag=[0-9]+_")
#/u/3738760754?refer_flag=1005050008_
#\/u\/3738760754?refer_flag=1005050008_\

links = soup.find_all("script")
for link in links:
    text = link.get_text()
    text = text.replace('\/', '\\')
#     print text


# links = soup.find_all("a",href=re.compile(r"\/u\/3738760754\?refer_flag=1005050008_"))

# print links


# strinfo = re.compile('href="\/u\/')
# b = strinfo.sub('href="/u/',a)
# print "b="+b
# b = re.compile(r"/u/[0-9]+\?refer_flag=[0-9]+_")
# href="/u/2515950453?refer_flag=1005050005_" class="S_txt1">段晓阳session</a>
a = ' href="/u/2515950453?refer_flag=1005050005_" class="S_txt1">段晓阳session</a> '
# print "a="+a
patten = re.compile(r'href="(\\/u\\/[0-9]+\?refer_flag=[0-9]+_)"')
b = patten.findall(a)
print b
bb = b[0].replace("\\","")
print bb
