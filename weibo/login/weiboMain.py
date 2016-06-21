# coding:utf8
'''
Created on 2016年4月11日

@author: wb-zhaohaibo
'''
from weibo.login.weiboLogin import WeiboLogin
from weibo.spider import url_manager
from weibo.spider import html_downloader
from weibo.spider import html_parser
from weibo.spider import html_outputer
import spynner
import time
from _pyio import open
from bs4 import BeautifulSoup

class WeiboMain(object):
    def __init__(self):
        #记录用户粉丝url
        self.fansUrls = url_manager.UrlManager()
        #记录用户首页url
        self.userUrls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.Output()
        self.fansCount = 0
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
        
                        
    def craw_user(self,user_url,count,userMaxCount):
        flag = 0
        #下载粉丝主页
        html_cont = self.downloader.download(user_url)
        self.outputer.user_html(html_cont)
        #获取用户信息详情页url
        detailUrl = self.parser.getDetailUrl(html_cont,user_url)
        #详情页url不为空
        if detailUrl != "":
            #下载详情页
            info_cont = self.downloader.download(detailUrl)
            #解析用户详细信息
            new_data = self.parser.parseUserDetail(info_cont)
            #保存用户url
            new_data["userUrl"] = user_url
            print "已爬取   %d 个粉丝信息" % count
            if count > userMaxCount:
                flag = 1
            count = count + 1
        else:
            new_data = {}
            flag = 0
        return new_data,flag,count
        
    def craw(self,root_url,userMaxCount,weiboMaxCount):
        #userMaxCount 控制爬取的微博用户最大数
        #weiboMaxCount 控制爬取的微博内容最大数
        #已爬取粉丝数
        count = 1
        #爬取微博最大数
        weiboCoubt = 0
        #爬取的页面数
        pageCount = 1
        #写入微博html的前半部
        self.outputer.output_weibo_cont_bef()
        #写入粉丝html的前半部
        self.outputer.output_weibo_fans_bef()
        #把当前主页加入到粉丝主页列表
        self.fansUrls.add_new_fans_url(root_url)
        #判断粉丝列表是否有内容  粉丝列表存储的就是用户的主页url
        while self.fansUrls.has_new_fans_url():
            #休眠10秒钟
            print "程序休眠10秒钟。。。"
            time.sleep(10)
            try:
                new_user_url = self.fansUrls.get_new_fans_url()
                #获取用户主页的粉丝页面url--这是一个临时的url 不做存储  每个用户主页唯一对应一个粉丝页面url
                fansUrl = self.parser.getFansUrl(new_user_url)
                print "爬取第   %d 个粉丝页面地址: %s" % (pageCount,fansUrl)
#                 fansUrl = "http://weibo.com/p/1005052739250252/follow?relate=fans&from=100505&wvr=6&mod=headfans&current=fans#place"
                #下载个人页面粉丝页面信息
                html_cont = self.downloader.download(fansUrl)
                #输出个人页面粉丝页面信息
                self.outputer.text_html(html_cont)
                #获取粉丝主页地址
                new_user_urls = self.parser.parse(fansUrl,html_cont)
                if len(new_user_urls) == 0:
                    print "粉丝列表加载失败"
                else:
                    print "粉丝列表加载成功"
                #把新抓取的粉丝主页添加到用户主页url列表中
                self.fansUrls.add_new_fans_urls(new_user_urls)
                pageCount = pageCount + 1
                obj_spider = WeiboMain()
                for user_url in new_user_urls:
                    #爬取粉丝基本信息
                    new_data,flag,count = obj_spider.craw_user(user_url,count,userMaxCount)
                    #爬取发表的微博信息 list
                    weibo_conts = obj_spider.craw_weiboCont(user_url)
                    #收集用户数据
                    self.outputer.collect_data(new_data)
                    #写入发表微博信息  只包含table内容部分
                    #如果发表数过少  过滤掉不获取微博内容
                    if len(weibo_conts) >= 10 :
                        subCount = self.outputer.output_weibo_cont_html(weibo_conts)
                        weiboCoubt = weiboCoubt + subCount
                        print "已爬取微博数：%d" % weiboCoubt
                        #如果超过限定数量的微博已经爬取 则结束
                        if weiboCoubt >= weiboMaxCount:
                            flag = 1
                    if(flag == 1):
                        break
                #写入粉丝基本信息
                self.outputer.output_fans_html()
                #到达预设记录数 结束爬取
                if(flag == 1):
                    #写入微博内容html的后半部
                    self.outputer.output_weibo_cont_beh()
                    #写入微博粉丝html的后半部
                    self.outputer.output_weibo_fans_beh()
                    print "所有记录爬取完成！共爬取 %d 条微博！" % weiboCoubt
                    break
            except Exception as e:
                print "该用户记录爬取失败！"
                print "weiboMain.craw:" + str(e)

    
    def craw_weiboCont(self, rootUrl):
        try:
            weibo_data = []
            #下载微博主页页面信息
            html_cont = self.downloader.download(rootUrl)
            soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
            tags = soup.findAll("script")
            if len(tags) > 1:
                #获取包含微博内容的script
                tag = tags[len(tags)-2].get_text()
                indexBegin = tag.find("<div")
                indexEnd = tag.rfind("<\/div>")#从
                if indexBegin != -1 and indexEnd != -1:
                    contStr = tag[indexBegin:indexEnd+7]
                    #写入到临时网页中 weibo_temp.html
                    self.outputer.output_weibo_temp(contStr)
                    #获取临时文件 提取微博内容
                    weibo_data = self.parser.getWeiboCont()
                else:
                    #未发表微博
                    pass
            else:
                print "微博内容爬取失败"
        except Exception as e:
            print "获取微博内容出错!"
            print "weiboMain.craw_weiboCont:"+str(e)
            raise e
        return weibo_data
            
            
    
    
if __name__ == '__main__':
    startTime = time.time()
    username = '1069757861@qq.com'
    password = 's123456'
    weiboLogin = WeiboLogin(username, password)
#     weiboLogin = WeiboLogin('798102408@qq.com', 'fsrm113312..1')#邮箱（账号）、密码
    if weiboLogin.Login() != True:
        print "登录失败!"
    else:
        print "登陆成功！username = "+username
        #正式访问
        #主页地址
        rootUrl = "http://weibo.com/u/5296704009?refer_flag=1005050012_"
        obj_spider = WeiboMain()
        #启动爬虫  rootUrl为用户主页
        #微博用户最大数限制
        userMaxCount = 1000
        #微博内容最大数限制
        weiboMaxCount = 1000
        obj_spider.craw(rootUrl,userMaxCount,weiboMaxCount)
    endTime = time.time()
    si = endTime - startTime
    mi = (si % 3600)/60
    hi = si/3600
    
    print "系统共耗时 %d 秒" % si
    print "系统共耗时 %d 时  %d 分" % (hi,mi)
        
#         #测试下载用户基本信息详情页
#         html_download = html_downloader.HtmlDownloader()
#         html_out = html_outputer.Output()
#         url = "http://weibo.com/p/1005055898067337/info?mod=pedit_more"
#         html_cont = html_download.download(url)
#         html_out.userDetail_html(html_cont)
        
#         #测试下载主页信息  获取微博内容
#         html_download = html_downloader.HtmlDownloader()
#         html_out = html_outputer.Output()
#         url = "http://weibo.com/u/2515950453?refer_flag=1005050005_&is_all=1"
#         html_cont = html_download.download(url)
#         html_out.user_html(html_cont)
        
        
        
        
