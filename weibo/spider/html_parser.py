# coding:utf8
'''
Created on 2016年4月8日

@author: wb-zhaohaibo
'''
from bs4 import BeautifulSoup
import re
import urlparse
import urllib
from weibo.spider import html_outputer, html_downloader

#html 解析器
class HtmlParser(object):
    def __init__(self):
        self.html_outputer = html_outputer.Output()
        self.html_downloader = html_downloader.HtmlDownloader()
        self.fans_data = {}
    
    
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
    #改动版  获取粉丝主页地址    并存入文件
    def _get_new_urls3(self, page_url, html_cont):
        new_urls = set()
        patten = re.compile(r'href=\\"(\\/u\\/[\d]+\?refer_flag=[\d]+_)\\"')
        hrefs = patten.findall(html_cont);
        if len(hrefs) != 0:
            count = 0
            for href in hrefs:
                href = href.replace("\\","")
                new_urls.add("http://weibo.com"+href+"&is_hot=1")
                count = count + 1
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
    
    #获取微博用户个人信息详细页面url地址
    def getDetailUrl(self,html_cont,user_url):
#         soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
        #<a class="WB_cardmore S_txt1 S_line1 clearfix" href="/p/1005053842859029/info?mod=pedit_more" bpfilter="page_frame" ontouchstart="">
        #<a href=\"http:\/\/weibo.com\/p\/1005052515950453\/album?from=profile_right#wbphoto_nav\" class=\"WB_cardmore S_txt1 S_line1 clearfix\">
        patten = re.compile(r'href=\\"(\\/p\\/[0-9]+\\/info\?mod=pedit_more)\\"')
        moreStr = patten.findall(html_cont)
        str_ = ""
        if len(moreStr) != 0:
            str_ = moreStr[0].replace("\\","")
            str_ = "http://weibo.com"+str_
        else:
            print "获取用户信息详情失败！！！user_url="+user_url
        return str_    
        
    #解析分析主页 获取粉丝基本信息
    def parseUserDetail(self,info_cont):
        fans_data = {}
        try:
            
            #保存本地临时文件 
            self.html_outputer.userDetail_html(info_cont)
            #读取保存的文件信息
            link = open("userDetail.html").read().decode("utf8")
            #解析出用户基本信息
            #获取昵称
            pattenNickName = re.compile(ur'<span class=\\"pt_title S_txt2\\">昵称：<\\/span><span class=\\"pt_detail\\">([[\u4e00-\u9fa5\w_\-]+)<\\/span>')
            nickNames = pattenNickName.findall(link)
            if len(nickNames) != 0:
                nickName = nickNames[0]
            else:
                nickName = ""
            fans_data["nickName"] = nickName
            #获取所在地
            pattenLocation = re.compile(ur'<span class=\\"pt_title S_txt2\\">所在地：<\\/span><span class=\\"pt_detail\\">([\u4e00-\u9fa5\w\s_]+)<\\/span>')
            locations = pattenLocation.findall(link)
            if len(locations) != 0:
                location = locations[0]
            else:
                location = ""
            fans_data["location"] = location
            #获取性别
            pattenSex = re.compile(ur'<span class=\\"pt_title S_txt2\\">性别：<\\/span><span class=\\"pt_detail\\">([\u4e00-\u9fa5]{1})<\\/span>')
            sexs = pattenSex.findall(link)
            if len(sexs) != 0:
                sex = sexs[0]
            else:
                sex = ""
            fans_data["sex"] = sex
            #获取性取向
            pattenSexOri = re.compile(ur'<span class=\\"pt_title S_txt2\\">性取向：<\\/span>[\\r]*[\\n]*[\\t]*<span class=\\"pt_detail\\">[\\r]*[\\n]*[\\t]*([\u4e00-\u9fa5]+)[\\r]*[\\n]*[\\t]*<\\/span>')
            sexOris = pattenSexOri.findall(link)
            if len(sexOris) != 0:
                sexOri = sexOris[0]
            else:
                sexOri = ""
            fans_data["sexOri"] = sexOri
            #获取感情状况
            pattenEmotion = re.compile(ur'<span class=\\"pt_title S_txt2\\">感情状况：<\\/span>[\\r]*[\\n]*[\\t]*<span class=\\"pt_detail\\">[\\r]*[\\n]*[\\t]*([\u4e00-\u9fa5]+)[\\r]*[\\n]*[\\t]*<\\/span>')
            emotions = pattenEmotion.findall(link)
            if len(emotions) != 0:
                emotion = emotions[0]
            else:
                emotion = ""
            fans_data["emotion"] = emotion
            #获取生日信息
            pattenBirthDay = re.compile(ur'<span class=\\"pt_title S_txt2\\">生日：<\\/span><span class=\\"pt_detail\\">([\u4e00-\u9fa5\d]+)<\\/span>')
            birthDays = pattenBirthDay.findall(link)
            if len(birthDays) != 0:
                birthDay = birthDays[0]
            else:
                birthDay = ""
            fans_data["birthDay"] = birthDay
            #获取血型
            pattenBloodType = re.compile(ur'<span class=\\"pt_title S_txt2\\">血型：<\\/span><span class=\\"pt_detail\\">([a-zA-Z]+)<\\/span>')
            bloodTypes = pattenBloodType.findall(link)
            if len(bloodTypes) != 0:
                bloodType = bloodTypes[0]
            else:
                bloodType = ""
            fans_data["bloodType"] = bloodType
            #获取注册时间
            pattenRegisterDate = re.compile(ur'<span class=\\"pt_title S_txt2\\">注册时间：<\\/span>[\\r]*[\\n]*[\\t]*<span class=\\"pt_detail\\">[\\r]*[\\n]*[\\t]*([-\d]+)[\\r]*[\\n]*[\\t]*<\\/span>')
            registerDates = pattenRegisterDate.findall(link)
            if len(registerDates) != 0:
                registerDate = registerDates[0]
            else:
                registerDate = ""
            fans_data["registerDate"] = registerDate
            #获取联系相关信息
            #获取邮箱信息
            pattenEmail = re.compile(ur'<span class=\\"pt_title S_txt2\\">邮箱：<\\/span><span class=\\"pt_detail\\">([\w\.@_#&]+)<\\/span>')
            emails = pattenEmail.findall(link)
            if len(emails) != 0:
                email = emails[0]
            else:
                email = ""
            fans_data["email"] = email
            #获取QQ号码
            pattenQQ = re.compile(ur'<span class=\\"pt_title S_txt2\\">QQ：<\\/span>[\\r\\n\\t\s]*<span class=\\"pt_detail\\">([\d]*)<\\/span>')
            QQs = pattenQQ.findall(link)
            if len(QQs) != 0:
                QQ = QQs[0]
            else:
                QQ = ""
            fans_data["QQ"] = QQ
            #获取教育信息  大学
            pattenUniversity = re.compile(ur'<span class=\\"pt_title S_txt2\\">大学：<\\/span>[\\r\\n\\t]*<span class=\\"pt_detail\\">[\\r\\n\\t]*<a href=\\"http:\\/\\/s\.weibo\.com\\/user\\/&school=[\w%&=]+\\">([\u4e00-\u9fa5]+)<\\/a>')
            universitys = pattenUniversity.findall(link)
            if len(universitys) != 0:
                university = universitys[0]
            else:
                university = ""
            fans_data["university"] = university
            #获取教育信息  高中
            pattenHignSchool = re.compile(ur'<span class=\\"pt_title S_txt2\\">高中：<\\/span>[\\r\\n\\t]*<span class=\\"pt_detail\\">[\\r\\n\\t]*<a href=\\"http:\\/\\/s\.weibo\.com\\/user\\/&school=[\w%&=]+\\">([\u4e00-\u9fa5]+)<\\/a>')
            hignSchools = pattenHignSchool.findall(link)
            if len(hignSchools) != 0:
                hignSchool = hignSchools[0]
            else:
                hignSchool = ""
            fans_data["hignSchool"] = hignSchool
            #获取教育信息  初中
            pattenJuniorSchool = re.compile(ur'<span class=\\"pt_title S_txt2\\">初中：<\\/span>[\\r\\n\\t]*<span class=\\"pt_detail\\">[\\r\\n\\t]*<a href=\\"http:\\/\\/s\.weibo\.com\\/user\\/&school=[\w%&=]+\\">([\u4e00-\u9fa5]+)<\\/a>')
            juniorSchools = pattenJuniorSchool.findall(link)
            if len(juniorSchools) != 0:
                juniorSchool = juniorSchools[0]
            else:
                juniorSchool = ""
            fans_data["juniorSchool"] = juniorSchool
            #获取工作信息
            pattenCompany = re.compile(ur'<span class=\\"pt_detail\\">[\\r\\n\\t]*<a href=\\"http:\\/\\/s\.weibo\.com\\/user\\/&work=[\w%&=]+\\" target=\\"_blank\\">([\u4e00-\u9fa5]+)<\\/a>')
            companys = pattenCompany.findall(link)
            length = len(companys)
            comp = ""
            if length != 0:
                for company in companys:
                    comp =comp + company + "," 
                comp = comp[0:len(comp)-1]
            else:
                comp = ""
            fans_data["company"] = comp    
            #获取标签信息
            pattenTag = re.compile(ur'href=\\"http:\\/\\/s\.weibo\.com\\/user\\/&tag=([\w%]+)\\"')
            tags = pattenTag.findall(link.encode("utf8"))
            length = len(tags)
            tagTemp = ""
            if length != 0:
                for tag in tags:
                    tag = urllib.unquote(tag)
                    tagTemp = tagTemp + tag + ","  
                tagTemp = tagTemp[0:len(tagTemp)-1]  
            else:
                tagTemp = ""
            fans_data["tags"] = tagTemp
        except Exception as e:
            print "用户详情获取出错！"
            print "html_parser.parseUserDetail:" + str(e)
        return fans_data
    
    def getFansUrl(self,root_url):
        #从主页获取粉丝页地址信息
        root_cont = self.html_downloader.download(root_url).decode("utf8")
        #输出用户主页信息
        self.html_outputer.user_html(root_cont)
        root_cont = open("user.html").read().decode("utf8")
#         soup = BeautifulSoup(root_cont,"html.parser",from_encoding="utf-8")
#         fansUrls = soup.findAll("a",class_="t_link S_txt1")
        patten = re.compile(ur'<a bpfilter=\\"page_frame\\"  class=\\"t_link S_txt1\\" href=\\"http:\\/\\/(weibo.com[\\/p]*\\/[0-9]+\\/[\?&=#a-zA-z0-9]+)\\" ><strong class=\\"W_f18\\">[0-9]*<\\/strong><span class=\\"S_txt2\\">[\u4e00-\u9fa5]+<\\/span><\\/a>')
        fansUrls = patten.findall(root_cont)
        length = len(fansUrls)
        if length == 3:
            #关注主页地址 第二个是粉丝信息 第三个是文章信息地址    
#             conUrl = fansUrls[0].replace("\/","/")
            #粉丝主页地址
            fansUrl = fansUrls[1].replace("\/","/")
            fansUrl = fansUrl.replace("\\n","")
            fansUrl = fansUrl.replace(" ","")
#             print "粉丝主页地址"+str(fansUrl) 
            #文章列表地址
#             ortUrl = fansUrls[2].replace("\/","/")
        else:
            print "获取粉丝主页地址失败！length= %d" % length
        return "http://"+fansUrl

    #获取微博内容 并存储
    def getWeiboCont(self):
        "获取微博发表的内容"
        try:
            weibo_datas = []
            html_cont = open("output_weibo_temp.html","r").read()
            soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
            conts = soup.findAll("div",class_="WB_detail")
            length = len(conts)
            if length != 0:
                count = 0
                for cont in conts:
                    weibo_data = {}
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
                        textTag = textExpand.find("div",class_="WB_expand S_bg1").find("div",class_="WB_text")
                        if textTag is not None:
                            text = "//"+textTag.get_text()
                    text = myText + text
                    text = text.replace("\\t","")
                    text = text.replace("\\n","")
                    weibo_data["name"] = name
                    weibo_data["time"] = time
                    weibo_data["text"] = text
                    weibo_datas.append(weibo_data)
            else:
                print "该用户没有发表微博！！"
        except Exception as e:
            print "获取微博发表的内容失败!"
            print "html_parser.getWeiboCont:"+str(e)
        return weibo_datas
    
    
    



