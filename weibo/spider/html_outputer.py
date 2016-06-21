# coding:utf8
'''
Created on 2016年4月8日

@author: wb-zhaohaibo
'''

#输出器
class Output(object):
    def __init__(self):
        self.fans_count = 0
        self.weibo_count = 0
        self.datas = []
        self.user_old_datas = []
        self.weibo_datas = []
    #收集数据
    def collect_data(self,data):
        if data is None or len(data) == 0:
            return 
        if data not in self.datas:
            self.datas.append(data)
    #收集微博数据
    def collect_weibo_data(self,data):
        if data is None:
            return 
        self.weibo_datas.append(data)
    
    #写出数据到html
    def output_html(self):
        file_out = open("output.html","w")
        file_out.write("<html>")
        file_out.write("<head><meta http-equiv='Content-Type' content='text/html; charset=utf-8'/></head>")
        file_out.write("<body>")
        file_out.write("<table>")
        
        for data in self.datas:
            file_out.write("<tr>")
            file_out.write("<td>%s</td>" % data["url"])
            file_out.write("<td>%s</td>" % data["title"])
            file_out.write("<td>%s</td>" % data["data"])
            file_out.write("</tr>")
        
        file_out.write("</table>")
        file_out.write("</body>")
        file_out.write("</html>")
        file_out.close()
    def output_weibo_fans_bef(self):
        #写入粉丝文件头
        file_out = open("output_fans.html","w")
        file_out.write("<html>\n")
        file_out.write("<head><meta http-equiv='Content-Type' content='text/html; charset=utf-8'/></head>\n")
        file_out.write("<body>\n")
        file_out.write("\t<table border='1'cellspacing='0' cellpadding='0'>\n")
        file_out.write("\t\t<tr>\n")
        file_out.write("\t\t\t<td>序号</td>\n")
        file_out.write("\t\t\t<td>微博昵称</td>\n")
        file_out.write("\t\t\t<td>地址</td>\n")
        file_out.write("\t\t\t<td>性别</td>\n")
        file_out.write("\t\t\t<td>性取向</td>\n")
        file_out.write("\t\t\t<td>感情状态</td>\n")
        file_out.write("\t\t\t<td>生日</td>\n")
        file_out.write("\t\t\t<td>血型</td>\n")
        file_out.write("\t\t\t<td>注册日期</td>\n")
        file_out.write("\t\t\t<td>邮箱地址</td>\n")
        file_out.write("\t\t\t<td>QQ号码</td>\n")
        file_out.write("\t\t\t<td>大学</td>\n")
        file_out.write("\t\t\t<td>高中</td>\n")
        file_out.write("\t\t\t<td>初中</td>\n")
        file_out.write("\t\t\t<td>公司</td>\n")
        file_out.write("\t\t\t<td>标签</td>\n")
        file_out.write("\t\t\t<td>主页地址</td>\n")
        file_out.write("\t\t</tr>")
        file_out.close()
    #写出数据到html
    def output_fans_html(self):
        file_out = open("output_fans.html","a")
        for data in self.datas:
            self.fans_count = self.fans_count + 1
            file_out.write("\t\t<tr>\n")
            file_out.write("\t\t\t<td>%d</td>\n" % self.fans_count)
            file_out.write("\t\t\t<td>%s</td>\n" % data["nickName"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["location"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["sex"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["sexOri"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["emotion"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["birthDay"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["bloodType"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["registerDate"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["email"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["QQ"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["university"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["hignSchool"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["juniorSchool"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["company"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["tags"])
            file_out.write("\t\t\t<td>%s</td>\n" % data["userUrl"])
            file_out.write("\t\t</tr>")
    def output_weibo_fans_beh(self):
        file_out = open("output_fans.html","a")
        file_out.write("\t</table>\n")
        file_out.write("</body>\n")
        file_out.write("</html>")
        file_out.close()
    def output_weibo_cont_bef(self):
        file_out = open("output_weibo_cont.html","w")
        file_out.write("<html>\n")
        file_out.write("<head><meta http-equiv='Content-Type' content='text/html; charset=utf-8'/></head>\n")
        file_out.write("<body>\n")
        file_out.write("\t<table border='1'cellspacing='0' cellpadding='0'>\n")
        file_out.write("\t\t<tr>\n")
        file_out.write("\t\t\t<td>序号</td>\n")
        file_out.write("\t\t\t<td>微博昵称</td>\n")
        file_out.write("\t\t\t<td>时间</td>\n")
        file_out.write("\t\t\t<td>微博内容</td>\n")
        file_out.write("\t\t</tr>")
        file_out.close()
    #写出微博数据到html
    def output_weibo_cont_html(self,weibo_conts):
        file_out = open("output_weibo_cont.html","a")
        #记录已爬取的微博数
        length = 0
        for data in weibo_conts:
            if len(data) != 0:
                length = length + 1
                self.weibo_count = self.weibo_count + 1
                file_out.write("\t\t<tr>\n")
                file_out.write("\t\t\t<td>%d</td>\n" % self.weibo_count)
                file_out.write("\t\t\t<td>%s</td>\n" % data["name"])
                file_out.write("\t\t\t<td>%s</td>\n" % data["time"])
                file_out.write("\t\t\t<td>%s</td>\n" % data["text"])
                file_out.write("\t\t</tr>")
            else:
                #do nothing
                print "空记录微博"
        file_out.close()
        print "该用户微博写入成功！"
        return length
    def output_weibo_cont_beh(self):
        file_out = open("output_weibo_cont.html","a")
        file_out.write("\t</table>\n")
        file_out.write("</body>\n")
        file_out.write("</html>")
        file_out.close()
    def text_html(self,html_cont):
        file_out = open("text.html","w")
        file_out.write(html_cont)
        file_out.close()
    #输出用户主页信息
    def user_html(self,html_cont):
        file_out = open("user.html","w")
        file_out.write(html_cont)
        file_out.close()
    #输出用户基本信息详情页    
    def userDetail_html(self,html_cont):
        file_out = open("userDetail.html","w")
        file_out.write(html_cont)
        file_out.close()

    #输出微博html到临时文件
    def output_weibo_temp(self,html_cont):
        html_cont = html_cont.replace('\\"','"')
        html_cont = html_cont.replace('\\n','')
        html_cont = html_cont.replace('\\r','')
        html_cont = html_cont.replace('\\t','')
        html_cont = html_cont.replace('\\/','/')
        file_out = open("output_weibo_temp.html","w")
        file_out.write("<html>\n")
        file_out.write("<head><meta http-equiv='Content-Type' content='text/html; charset=utf-8'/></head>\n")
        file_out.write("<body>\n")
        file_out.write(html_cont)
        file_out.write("</body>\n")
        file_out.write("</html>")
        file_out.close()

    
    
    
    
    
    
    



