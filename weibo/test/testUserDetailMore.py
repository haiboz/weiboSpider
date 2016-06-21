#coding:utf8
'''
Created on 2016年4月14日

@author: wb-zhaohaibo
'''
import urllib
import re
html_cont = open("userDetail.html").read().decode("utf8")
# [\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?
pattenEmail = re.compile(ur'<span class=\\"pt_title S_txt2\\">邮箱：<\\/span><span class=\\"pt_detail\\">([\w\.@_#&]+)<\\/span>')
emails = pattenEmail.findall(html_cont)
print emails[0]

#<span class=\"pt_title S_txt2\">QQ：<\/span>\r\n        \t\t\t\t\t\t\t<span class=\"pt_detail\">513643468<\/span>
pattenQQ = re.compile(ur'<span class=\\"pt_title S_txt2\\">QQ：<\\/span>[\\r\\n\\t\s]*<span class=\\"pt_detail\\">([\d]*)<\\/span>')
QQs = pattenQQ.findall(html_cont)
print QQs[0]
#<span class=\"pt_title S_txt2\">大学：<\/span>\r\n\t\t\t\t\t\t\t\t<span class=\"pt_detail\">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href=\"http:\/\/s.weibo.com\/user\/&school=%E9%BB%84%E6%B7%AE%E5%AD%A6%E9%99%A2&from=inf&wvr=5&loc=infedu\">黄淮学院<\/a> (2010年)\t\t\t\t\t\t\t\t\t<br\/>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   信息工程系\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<\/span>
pattenSchool = re.compile(ur'<span class=\\"pt_title S_txt2\\">大学：<\\/span>[\\r\\n\\t]*<span class=\\"pt_detail\\">[\\r\\n\\t]*<a href=\\"http:\\/\\/s\.weibo\.com\\/user\\/&school=[\w%&=]+\\">([\u4e00-\u9fa5]+)<\\/a>')
schools = pattenSchool.findall(html_cont)
print schools[0]
#<span class=\"pt_title S_txt2\">高中：<\/span>\r\n\t\t\t\t\t\t\t\t<span class=\"pt_detail\">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href=\"http:\/\/s.weibo.com\/user\/&school=%E8%AE%B8%E6%98%8C%E9%AB%98%E4%B8%AD&from=inf&wvr=5&loc=infedu\">许昌高中<\/a> (2007年)\t\t\t\t\t\t\t\t\t<br\/>
pattenHignSchool = re.compile(ur'<span class=\\"pt_title S_txt2\\">高中：<\\/span>[\\r\\n\\t]*<span class=\\"pt_detail\\">[\\r\\n\\t]*<a href=\\"http:\\/\\/s\.weibo\.com\\/user\\/&school=[\w%&=]+\\">([\u4e00-\u9fa5]+)<\\/a>')
hignSchools = pattenHignSchool.findall(html_cont)
print hignSchools[0]
#<span class=\"pt_title S_txt2\">初中：<\/span>\r\n\t\t\t\t\t\t\t\t<span class=\"pt_detail\">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href=\"http:\/\/s.weibo.com\/user\/&school=%E8%A7%A3%E6%94%BE%E4%B8%AD%E5%AD%A6%E5%88%86%E6%A0%A1&from=inf&wvr=5&loc=infedu\">解放中学分校<\/a>
pattenHignSchool = re.compile(ur'<span class=\\"pt_title S_txt2\\">初中：<\\/span>[\\r\\n\\t]*<span class=\\"pt_detail\\">[\\r\\n\\t]*<a href=\\"http:\\/\\/s\.weibo\.com\\/user\\/&school=[\w%&=]+\\">([\u4e00-\u9fa5]+)<\\/a>')
hignSchools = pattenHignSchool.findall(html_cont)
print hignSchools[0]
#<span class=\"pt_detail\">\r\n\t\t\t\t\t\t\t\t\t\t<a href=\"http:\/\/s.weibo.com\/user\/&work=%E6%B5%99%E6%B1%9F%E6%9C%97%E6%96%B0%E7%A7%91%E6%8A%80&from=inf&wvr=5&loc=infjob\" target=\"_blank\">浙江朗新科技<\/a>
pattenCompany = re.compile(ur'<span class=\\"pt_detail\\">[\\r\\n\\t]*<a href=\\"http:\\/\\/s\.weibo\.com\\/user\\/&work=[\w%&=]+\\" target=\\"_blank\\">([\u4e00-\u9fa5]+)<\\/a>')
companys = pattenCompany.findall(html_cont)
length = len(companys)
comp = ""
if length != 0:
    for company in companys:
        comp =comp + company + "," 
    comp = comp[0:len(comp)-1]
print comp

#href=\"http:\/\/s.weibo.com\/user\/&tag=%E8%BD%AF%E4%BB%B6\"
pattenTag = re.compile(ur'href=\\"http:\\/\\/s\.weibo\.com\\/user\\/&tag=([\w%]+)\\"')
tags = pattenTag.findall(html_cont.encode("utf8"))
length = len(tags)
tagTemp = ""
if length != 0:
    for tag in tags:
        tag = urllib.unquote(tag)
        tagTemp = tagTemp + tag + ","  
    tagTemp = tagTemp[0:len(tagTemp)-1]  
print tagTemp













