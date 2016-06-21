#encoding:utf8
'''
Created on 2016年4月11日

@author: wb-zhaohaibo
'''

import spynner


  
if __name__ == '__main__':
    browser = spynner.Browser()  
    #创建一个浏览器对象  
      
    browser.hide()  
    #打开浏览器，并隐藏。  
      
    browser.load("http://www.weather.com.cn/weather/101070105.shtml")  
    #browser 类中有一个类方法load，可以用webkit加载你想加载的页面信息。  
    #load(是你想要加载的网址的字符串形式)  
      
    print browser.html.encode("utf-8")  
    #browser 类中有一个成员是html，是页面进过处理后的源码的字符串.  
    #将其转码为UTF-8编码  
      
    htmlContent = open("Test.html", 'w+').write(browser.html.encode("utf-8"))   
    #你也可以将它写到文件中，用浏览器打开。  
    print htmlContent
      
    browser.close()    