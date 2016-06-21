#encoding:utf8
'''
Created on 2016年4月12日

@author: wb-zhaohaibo
'''
import re
from bs4 import BeautifulSoup


html_cont = open("user.html","r").read().decode("utf8")
# soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
# <a class="WB_cardmore S_txt1 S_line1 clearfix" href="/p/1005053842859029/info?mod=pedit_more" bpfilter="page_frame" ontouchstart="">
#<a class=\"WB_cardmore S_txt1 S_line1 clearfix\" \r\n\t href=\"\/p\/1005052515950453\/info?mod=pedit_more\"\r\n\t\t    bpfilter=\"page_frame\"\r\n\t 
patten = re.compile(r'href="(\\/p\\/[0-9]+\\/info\?mod=pedit_more)"')
b = patten.findall(html_cont)
print b
#href=\"\/u\/3738760754?refer_flag=1005050008_\"
# patten = re.compile(r'href="(\\/u\\/[0-9]+\?refer_flag=[0-9]+_)"')
# mores = soup.find("a",class_="WB_cardmore S_txt1 S_line1 clearfix")
# more = mores[1]
# if more is not None:
#     print more
# pass


#测试获取用户粉丝主页url                            relate=fans&from=100505&wvr=6&mod=headfans&current=fans#place
#<a bpfilter=\"page_frame\"  class=\"t_link S_txt1\" href=\"http:\/\/weibo.com\/p\/1005055346699613\/follow?relate=fans&from=100505&wvr=6&mod=headfans&current=fans#place\" ><strong class=\"W_f18\">78<\/strong><span class=\"S_txt2\">粉丝<\/span><\/a>
patten2 = re.compile(ur'<a bpfilter=\\"page_frame\\"  class=\\"t_link S_txt1\\" href=\\"http:\\/\\/(weibo.com[\\/p]*\\/[0-9]+\\/[\?&=#a-zA-z0-9]+)\\" ><strong class=\\"W_f18\\">[0-9]*<\\/strong><span class=\\"S_txt2\\">[\u4e00-\u9fa5]+<\\/span><\\/a>')
b2 = patten2.findall(html_cont)
if len(b2) != 0:
    bb = b2[0].replace("\/","/")
    print bb


#<div class="WB_text" node-type="feed_list_reason">  <a target="_blank" render="ext" suda-uatrack="key=topic_click&amp;value=click_topic" class="a_topic" extra-data="type=topic" href="http://huati.weibo.com/k/%E5%92%8C%E9%A2%90%E9%85%92%E5%BA%97%E5%A5%B3%E7%94%9F%E9%81%87%E8%A2%AD?from=501">#和颐酒店女生遇袭#</a><a target="_blank" render="ext" suda-uatrack="key=topic_click&amp;value=click_topic" class="a_topic" extra-data="type=topic" href="http://huati.weibo.com/k/%E5%8D%96%E6%B7%AB%E7%AA%9D%E7%82%B9%E6%A1%88%E5%BA%95%E9%85%92%E5%BA%97?from=501">#卖淫窝点案底酒店#</a>整理了我被劫持的经过和事态发展到现在的结果，希望对看到这个文章的朋友有所帮助，并且让更多的人转发扩散，让身边的女生看到我的案子有警觉心，也希望有关部门看到这个文章之后，能给我一个有诚意的答复！<br>











