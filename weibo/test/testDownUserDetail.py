# coding:utf8
'''
Created on 2016年4月13日

@author: wb-zhaohaibo
'''
from weibo.spider import html_downloader, html_outputer


html_download = html_downloader.HtmlDownloader()
html_out = html_outputer.Output()

url = "http://weibo.com/p/1005053059519877/info?mod=pedit_more"
html_cont = html_download.download(url)

html_out.userDetail_html(html_cont)


