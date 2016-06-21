# coding:utf8
'''
Created on 2016年4月8日

@author: wb-zhaohaibo
'''

#url管理器

class UrlManager(object):
    
    def __init__(self):
        self.new_user_urls = set()
        self.old_user_urls = set()
        self.new_fans_urls = set()
        self.old_fans_urls = set()
    
    def add_new_user_url(self,url):
        if url is None:
            return 
        if url not in self.old_user_urls and url not in self.new_user_urls:
            self.new_user_urls.add(url)
    def add_new_fans_url(self,url):
        if url is None:
            return 
        if url not in self.old_fans_urls and url not in self.new_fans_urls:
            self.new_fans_urls.add(url)
    def add_new_user_urls(self,urls):
        if urls is None or len(urls) == 0:
            return 
        for url in urls:
            self.add_new_user_url(url)
    def add_new_fans_urls(self,urls):
        if urls is None or len(urls) == 0:
            return 
        for url in urls:
            self.add_new_fans_url(url)
    def has_new_user_url(self):
        return len(self.new_user_urls) != 0
    def has_new_fans_url(self):
        return len(self.new_fans_urls) != 0
    def get_new_user_url(self):
        #pop函数会选择一个并移除出列表
        new_url = self.new_user_urls.pop()
        self.old_user_urls.add(new_url)
        return new_url
    def get_new_fans_url(self):
        #pop函数会选择一个并移除出列表
        new_url = self.new_fans_urls.pop()
        self.old_fans_urls.add(new_url)
        return new_url
    
    
    
    
    
    
    
    
    
    



