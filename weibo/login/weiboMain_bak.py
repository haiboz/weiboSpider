# coding:utf8
'''
Created on 2016年4月11日

@author: wb-zhaohaibo
'''
import weiboLogin
# import urllib2
from weibo.spider import url_manager
from weibo.spider import html_downloader
from weibo.spider import html_parser
from weibo.spider import html_outputer
import spynner
from _pyio import open

class WeiboMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.Output()
    def parseDownPage(self,url):
        browser = spynner.Browser()  
        #创建一个浏览器对象  
          
        browser.hide()  
        #打开浏览器，并隐藏。  
          
        browser.load(url)  
        #browser 类中有一个类方法load，可以用webkit加载你想加载的页面信息。  
        #load(是你想要加载的网址的字符串形式)  
        htmlContent = browser.html.encode("utf-8")
#         htmlContent = open("Test.html", 'w+').write(browser.html.encode("utf-8"))   
        #你也可以将它写到文件中，用浏览器打开。  
        print "htmlContent="+htmlContent
        return htmlContent
        #browser 类中有一个成员是html，是页面进过处理后的源码的字符串.  
          
        htmlContent = open("Test.html", 'w+')  
    def craw_bak(self,root_url):
            count = 1
            self.urls.add_new_url(root_url)
            while self.urls.has_new_url():
                try:
                    new_url = self.urls.get_new_url()
                    print "craw %d : %s" % (count,new_url)
#                     html_cont = self.parseDownPage(new_url)
                    html_cont = self.downloader.download(new_url)
#                     print "html_cont="+html_cont
#                     file_out = open("text.html","w+")
#                     file_out.write(html_cont)
                    self.outputer.text_html(html_cont)
                    print "new_url="+new_url
                    new_urls,new_data = self.parser.parse(new_url,html_cont)
                    #批量添加urls
                    self.urls.add_new_urls(new_urls)
                    self.outputer.collect_data(new_data)
                    if(count == 100):
                        break
                    count = count + 1
                except:
                    print "发生异常  爬取失败"
            self.outputer.output_html()
    def craw_user(self,user_url):
        print "爬取粉丝信息"
        user_url = "http://weibo.com"+user_url
        res_data = {}
        #保存用户url
        res_data["user_url"] = user_url
        #下载粉丝主页
        html_cont = self.downloader.download(user_url)
        self.outputer.user_html(html_cont)
        #解析页面
        self.parser.parseUser(html_cont)
        
        
        
        
        
        
        
    def craw(self,root_url):
            count = 1
            self.urls.add_new_url(root_url)
            while self.urls.has_new_url():
                try:
                    new_url = self.urls.get_new_url()
                    print "craw %d : %s" % (count,new_url)
                    html_cont = self.downloader.download(new_url)
                    self.outputer.text_html(html_cont)
                    print "new_url="+new_url
                    new_urls = self.parser.parse(new_url,html_cont)
                    #批量添加urls
                    self.urls.add_new_urls(new_urls)
                    obj_spider = WeiboMain()
                    for user_url in new_urls:
                        #爬取粉丝信息
                        obj_spider.craw_user(user_url)
                    if(count == 100):
                        break
                    count = count + 1
                except:
                    print "发生异常  爬取失败"
            self.outputer.output_html()
if __name__ == '__main__':
    weiboLogin = weiboLogin.WeiboLogin('798102408@qq.com', 'fsrm113312..1')#邮箱（账号）、密码
    if weiboLogin.Login() != True:
        print "登录失败!"
    else:
        print "登陆成功！"
        rootUrl = "http://weibo.com/2739250252/fans?from=100505&wvr=6&mod=headfans&current=fans#place"
#         rootUrl = "http://beian.hndrc.gov.cn/indexinvestment.jsp?id=162518"
#         htmlContent = urllib2.urlopen(rootUrl).read()#得到myurl网页的所有内容(html)
        obj_spider = WeiboMain()
        #启动爬虫
        obj_spider.craw(rootUrl)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        