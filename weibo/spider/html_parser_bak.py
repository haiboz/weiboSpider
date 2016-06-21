# coding:utf8
'''
Created on 2016年4月8日

@author: wb-zhaohaibo
'''
from bs4 import BeautifulSoup
import re
import urlparse

#html 解析器
class HtmlParser(object):
    
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /view/123.htm
        links = soup.find_all("a",href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link["href"]
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
#     改动版
    def _get_new_urls2(self, page_url, soup):
        new_urls = set()
        #<a class="S_txt1" target="_blank" usercard="id=1673748985&amp;refer_flag=1005050008_" href="/u/1673748985?refer_flag=1005050008_">liandie5200</a>
#         re_exp = re.compile(r"/u/[0-9]+\?refer_flag=[0-9]+_")
#         links = soup.find_all("link",rel="dns-prefetch")
#         links = soup.find_all("a",href=re.compile(r"/u/[0-9]+\?refer_flag=[0-9]+_"))
        links = soup.find_all("a",href=re.compile(r'href="(\\/u\\/[0-9]+\?refer_flag=[0-9]+[_]*)"'))
#         patten = re.compile(r'href="\\/u\\/[0-9]+\?refer_flag=[0-9]+_"')
#         b = patten.findall(a)
        print "page_url="+page_url
        if len(links) != 0:
            for link in links:
                new_url = link["href"]
                new_full_url = urlparse.urljoin(page_url, new_url)
    #             new_full_url = new_url
                new_urls.add(new_full_url)
        return new_urls
    #     改动版  获取粉丝id 并存入文件
    def _get_new_urls3(self, page_url, html_cont):
        new_urls = set()
        
        patten = re.compile(r'href=\\"(\\/u\\/[\d]+\?refer_flag=[\d]+_)\\"')
        hrefs = patten.findall(html_cont);
        if len(hrefs) != 0:
            print len(hrefs)
            count = 0
            for href in hrefs:
                href = href.replace("\\","")
                new_urls.add(href)
                count = count + 1
            print new_urls
            
            print count
        return new_urls
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data["url"] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find("h1")
        
        #<a href="/n?cmd=1&amp;class=chinasoccer&amp;pn=1" target="_self" class="group-title subnavcurrent">国内足球</a>
#         title_node = soup.find("a",class_="title")
        if title_node is not None:
            res_data["title"] = title_node.get_text()
        if title_node is None:
            res_data["title"] = "none"  
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find("div",class_="lemma-summary")
#         summary_node = soup.find("p")
        res_data["summary"] = summary_node.get_text()
        
        return res_data
    
    def _get_new_data2(self, page_url, soup):
        res_data = {}
        res_data["url"] = page_url
        #<h1 class="ts z">
        title_nodes = soup.find("a",class_="S_txt1")
        title_node = title_nodes[1]
        #<a href="/n?cmd=1&amp;class=chinasoccer&amp;pn=1" target="_self" class="group-title subnavcurrent">国内足球</a>
#         title_node = soup.find("a",class_="title")
        if title_node is not None:
            res_data["title"] = title_node.get_text()
        if title_node is None:
            res_data["title"] = "none"  
        #<div class="info_add"><em class="tit S_txt2">地址</em><span>重庆 南岸区</span></div>
        summary_node = soup.find("div",class_="info_add").find("span")
#         summary_node = soup.find("p")
        res_data["data"] = summary_node.get_text()
        
        return res_data
        
    def parse_bak(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
#         new_urls = self._get_new_urls2(page_url,soup)
        new_urls = self._get_new_urls3(page_url,html_cont)
        new_data = self._get_new_data2(page_url,soup)
        return new_urls,new_data
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        new_urls = self._get_new_urls3(page_url,html_cont)
        return new_urls

    #解析分析主页 获取粉丝基本信息
    def parseUser(self,html_cont):
        soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
        #<a class="WB_cardmore S_txt1 S_line1 clearfix" href="/p/1005053842859029/info?mod=pedit_more" bpfilter="page_frame" ontouchstart="">
        #<a href=\"http:\/\/weibo.com\/p\/1005052515950453\/album?from=profile_right#wbphoto_nav\" class=\"WB_cardmore S_txt1 S_line1 clearfix\">
        mores = soup.find("a",class_="WB_cardmore S_txt1 S_line1 clearfix")
        more = mores[1]
        if more is not None:
            print more
        pass
    
    



