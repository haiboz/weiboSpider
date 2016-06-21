#encoding:utf8
'''
Created on 2016年4月11日

@author: wb-zhaohaibo
'''

from weibo.spider import html_downloader

class Test(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        
    def craw(self,url):
        self.downloader.download(url)
if __name__ == '__main__':
    obj = Test
    obj.craw()
    
    