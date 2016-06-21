#encoding:utf8
'''
Created on 2016年4月12日

@author: wb-zhaohaibo
'''
import re
#http://weibo.com/u/5045053810?refer_flag=1005050005_&is_hot=1
#http://weibo.com/p/1005055045053810/info?mod=pedit_more

html_cont = open("text.html").read()
#href="/u/5710218160?refer_flag=1005050005_"
#href=\"\/u\/5775850992?from=myfollow_all\
patten = re.compile(r'href=\\"(\\/u\\/[\d]+\?refer_flag=[\d]+_)\\"')
hrefs = patten.findall(html_cont);
print hrefs