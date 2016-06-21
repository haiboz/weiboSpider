#encoding:utf8
'''
Created on 2016年4月11日

@author: wb-zhaohaibo
'''

from weibo.login.weiboLogin import WeiboLogin

class TestMain(object):
    def __init__(self):
#         self.weiboLogin = weiboLogin.WeiboLogin('1069757861@qq.com', 's123456',False)
        pass
    def craw(self):
        try:
            weiboLogin = WeiboLogin('1069757861@qq.com', 's123456')#邮箱（账号）、密码
            weiboLogin.Login()
        except Exception as e:
            print str(e)
    
if __name__ == '__main__':
    weiboLogin = WeiboLogin('1069757861@qq.com', 's123456')#邮箱（账号）、密码
    if weiboLogin.Login() != True:
        print "登录失败!"
    else:
        print "登陆成功！"
        #正式访问
        #主页地址
        rootUrl = "http://weibo.com/u/5296704009?refer_flag=1005050012_"
        obj_spider = TestMain()
        #启动爬虫  rootUrl为用户主页
        obj_spider.craw()
