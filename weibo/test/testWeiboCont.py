# coding:utf8
'''
Created on 2016年4月14日

@author: wb-zhaohaibo
'''
import re
# import urllib
from bs4 import BeautifulSoup
# import chardet
link = open("user.html").read().decode("utf8")
# <div class=\"WB_text W_f14\" node-type=\"feed_list_content\" >\n                                                                转发微博                            <\/div>
# <div class=\"WB_text W_f14\" node-type=\"feed_list_content\" nick-name=\"段晓阳session\">\n                                                                看完315的直播，又长了见识！                            <\/div>
# <div class=\"WB_text\" node-type=\"feed_list_reason\">\n                                                                <a target=\"_blank\" render=\"ext\" suda-uatrack=\"key=topic_click&value=click_topic\" class=\"a_topic\" extra-data=\"type=topic\" href=\"http:\/\/huati.weibo.com\/k\/%E5%92%8C%E9%A2%90%E9%85%92%E5%BA%97%E5%A5%B3%E7%94%9F%E9%81%87%E8%A2%AD?from=501\">#和颐酒店女生遇袭#<\/a><a target=\"_blank\" render=\"ext\" suda-uatrack=\"key=topic_click&value=click_topic\" class=\"a_topic\" extra-data=\"type=topic\" href=\"http:\/\/huati.weibo.com\/k\/%E5%8D%96%E6%B7%AB%E7%AA%9D%E7%82%B9%E6%A1%88%E5%BA%95%E9%85%92%E5%BA%97?from=501\">#卖淫窝点案底酒店#<\/a>整理了我被劫持的经过和事态发展到现在的结果，希望对看到这个文章的朋友有所帮助，并且让更多的人转发扩散，让身边的女生看到我的案子有警觉心，也希望有关部门看到这个文章之后，能给我一个有诚意的答复！<br>
# <div class=\"WB_text\" node-type=\"feed_list_reason\">\n                                                                “拾荒老人”名校毕业，遗产震惊世人。高山仰止，景行行止，虽不能至，心向往之。天堂，应该有您所在的图书馆的模样。
# <div class=\"WB_text\" node-type=\"feed_list_reason\">\n                                                                看完太愤怒！原来这就是被拐儿童的真相，也许我们做不了别的，但我们至少可以传.播出去，让更多的人重视起来！请扩散！！！
# <div class=\"WB_text\" node-type=\"feed_list_reason\">\n                                                                收废品的女老板曝出惊天内幕，震惊全国！真是太黑心了..<img render=\"ext\" src=\"http:\/\/img.t.sinajs.cn\/t4\/appstyle\/expression\/ext\/normal\/7c\/angrya_org.gif\" title=\"[怒]\" alt=    \"[怒]\" type=\"face\" \/> 活着真不容易&nbsp;&nbsp;&nbsp;且活且珍惜！！！<img render=\"ext\" src=\"http:\/\/img.t.sinajs.cn\/t4\/appstyle\/expression\/ext\/normal\/70\/88_org.gif\" title=\"[拜拜]\" alt=    \"[拜拜]\" type=\"face\" \/> 
# \\n\\r\\t\s\u4e00-\u9fa5
# <a target=\\"_blank\\" render=\\"ext\\" suda-uatrack=\\"key=topic_click&value=click_topic\\" class=\\"a_topic\\" extra-data=\\"type=topic\\" href=\\"http:\\/\\/huati\.weibo\.com\\/k\\/[%\?=\w]+\\">#(和颐酒店女生遇袭)#<\\/a>
# <a target=\\"_blank\\" render=\\"ext\\" suda-uatrack=\\"key=topic_click&value=click_topic\\" class=\\"a_topic\\" extra-data=\\"type=topic\\" href=\\"http:\\/\\/huati\.weibo\.com\\/k\\/[%\?=\w]+\\">#(卖淫窝点案底酒店)#<\\/a>
# 测试转发微博自填内容
# patten = re.compile(ur'<div class=\\"WB_text W_f14\\" node-type=\\"feed_list_content\\" [nick-name=\\"段晓阳session\\"]?>[\\n\\r\\t\s\u4e00-\u9fa5\w.，！:？]*[\u4e00-\u9fa5\w]*<\\/div>')
# 测试转发微博内容
patten = re.compile(ur'<div class=\\"WB_text\\" node-type=\\"feed_list_reason\\">\\n[\\n\\r\\t\s]*([\u4e00-\u9fa5。，！？：；“”‘’=-~\.]+)')
# 测试转发微博内容
# patten = re.compile(ur'<div class=\\"WB_text\\" node-type=\\"feed_list_reason\\">[\\n\\r\\t\s]*([\u4e00-\u9fa5。，！？：；“”‘’=-~.]+)')
# <a target=\"_blank\" render=\"ext\" suda-uatrack=\"key=topic_click&value=click_topic\" class=\"a_topic\" extra-data=\"type=topic\" href=\"http:\/\/huati.weibo.com\/k\/%E5%92%8C%E9%A2%90%E9%85%92%E5%BA%97%E5%A5%B3%E7%94%9F%E9%81%87%E8%A2%AD?from=501\">#和颐酒店女生遇袭#<\/a>
# <a target=\\"_blank\\" render=\\"ext\\" suda-uatrack=\\"key=topic_click&value=click_topic\\" class=\\"a_topic\\" extra-data=\\"type=topic\\" href=\\"http:\\/\\/huati\.weibo\.com\\/k\\/%\?=\w\\">
# [，。？：；‘’！“”—……、]|(－{2})|(（）)|(【】)|({})|(《》)
# [-,.?:;'"!`]|(-{2})|(/.{3})|(/(/))|(/[/])|({})
# [?,.;'\[\]{}~!@#$%^&*()_+|\-\\~！@#￥%……&*（）——+|、]
wbs = patten.findall(link)
length = len(wbs)
if wbs != 0:
    for wb in wbs:
        pass
#         print wb
# print wbs[0][0]
# print wbs[0][1]
# print wbs[0][2]
# print wbs[0][1]
# print wbs[0][2]
# print urllib.unquote(wbs[0])
# for wb in wbs:
#     wb = wb.replace("\\n","")
#     wb = wb.replace("  ","")
#    print wb

# tt = "整理了我被劫持的经过和事态发展到现在的结果，希望对看到这个文章的朋友有所帮助，并且让更多的人转发扩散，让身边的女生看到我的案子有警觉心，也希望有关部门看到这个文章之后，能给我一个有诚意的答复！"
# patten2 = re.compile(ur'[\u4e00-\u9fa5。，！]+')
# #[\u4e00-\u9fa5。，！]+
# ss = patten2.findall(tt.decode("utf8"))
# print ss[0]


# patten3 = re.compile(ur'<div class=\\"WB_text\\" node-type=\\"feed_list_reason\\">[\\n\\r\\t\s]*(<a target=\\"_blank\\" render=\\"ext\\" suda-uatrack=\\"key=topic_click&value=click_topic\\" class=\\"a_topic\\" extra-data=\\"type=topic\\" href=\\"http:\\/\\/huati\.weibo\.com\\/k\\/[%\?=\w]+\\">[#\u4e00-\u9fa5]*<\\/a>)*')
# wbs3 = patten3.findall(link)
# print wbs3
# print wbs3[0]
# print wbs3[1]
# print wbs3[2]


#-------------------测试获取html内容----------------------
#<div class="WB_text"
html_cont = open("test.html","r").read()
soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
conts = soup.findAll("div",class_="WB_detail")
length = len(conts)
print length
count = 0
for cont in conts:
    count = count + 1
    #<div class="WB_info">
    name = cont.find("div",class_="WB_info").get_text()
    #<div class="WB_from S_txt2">
    time = cont.find("div",class_="WB_from S_txt2").find("a").get_text()
    #<div class="WB_text W_f14"
    myText = cont.find("div",class_="WB_text W_f14").get_text()
    #<div class="WB_feed_expand">  <div class="WB_expand S_bg1" <div class="WB_text"
    textExpand = cont.find("div",class_="WB_feed_expand")
    if textExpand is None:
        text = ""
    else:
        text = "//"+textExpand.find("div",class_="WB_expand S_bg1").find("div",class_="WB_text").get_text()
    tempCont = name + " " + time +" " +myText+text
    tempCont = tempCont.replace("\t","")
    tempCont = tempCont.replace("\n","")
    print "第  %d 条: %s" % (count,tempCont)

    














