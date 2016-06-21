#encoding:utf8
'''
Created on 2016年4月13日

@author: wb-zhaohaibo
'''
import re
detail_cont = open("detail.html").read().decode('utf8')

#<span class=\"pt_title S_txt2\">昵称：<\/span><span class=\"pt_detail\">再见oo时光<\/span><\/li>
#[\u4e00-\u9fa5]*[\w]*
patten = re.compile(ur'<span class=\\"pt_title S_txt2\\">昵称：<\\/span><span class=\\"pt_detail\\">([\u4e00-\u9fa5\w_]+)<\\/span>')
b = patten.findall(detail_cont)
print b[0]
#<span class=\"pt_title S_txt2\">所在地：<\/span><span class=\"pt_detail\">青海 西宁<\/span>
patten2 = re.compile(ur'<span class=\\"pt_title S_txt2\\">所在地：<\\/span><span class=\\"pt_detail\\">([\u4e00-\u9fa5\w\s_]+)<\\/span>')
b2 = patten2.findall(detail_cont)
print b2[0]
#<span class=\"pt_title S_txt2\">性别：<\/span><span class=\"pt_detail\">男<\/span>
#<span class=\"pt_title S_txt2\">性别：<\/span><span class=\"pt_detail\">男<\/span>
patten3 = re.compile(ur'<span class=\\"pt_title S_txt2\\">性别：<\\/span><span class=\\"pt_detail\\">([\u4e00-\u9fa5]{1})<\\/span>')
b3 = patten3.findall(detail_cont)
print b3[0]
#<span class=\"pt_title S_txt2\">性取向：<\/span>\r\n\t\t\t\t\t\t\t\t<span class=\"pt_detail\">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t异性恋\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<\/span>
# patten4 = re.compile(ur'<span class=\\"pt_title S_txt2\\">性取向：<\\/span>\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t<span class=\\"pt_detail\\">\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t([\u4e00-\u9fa5]+)\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t<\\/span>')
patten4 = re.compile(ur'<span class=\\"pt_title S_txt2\\">性取向：<\\/span>[\\r]*[\\n]*[\\t]*<span class=\\"pt_detail\\">[\\r]*[\\n]*[\\t]*([\u4e00-\u9fa5]+)[\\r]*[\\n]*[\\t]*<\\/span>')
b4 = patten4.findall(detail_cont)
print b4[0]
#<span class=\"pt_title S_txt2\">感情状况：<\/span>\r\n\t\t\t\t\t\t\t\t\t<span class=\"pt_detail\">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t单身\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<\/span>
patten5 = re.compile(ur'<span class=\\"pt_title S_txt2\\">感情状况：<\\/span>[\\r]*[\\n]*[\\t]*<span class=\\"pt_detail\\">[\\r]*[\\n]*[\\t]*([\u4e00-\u9fa5]+)[\\r]*[\\n]*[\\t]*<\\/span>')
b5 = patten5.findall(detail_cont)
print b5[0]
#<span class=\"pt_title S_txt2\">生日：<\/span><span class=\"pt_detail\">1993年4月8日<\/span>
patten6 = re.compile(ur'<span class=\\"pt_title S_txt2\\">生日：<\\/span><span class=\\"pt_detail\\">([\u4e00-\u9fa5\d]+)<\\/span>')
b6 = patten6.findall(detail_cont)
print b6[0]
#<span class=\"pt_title S_txt2\">血型：<\/span><span class=\"pt_detail\">A<\/span>
patten7 = re.compile(ur'<span class=\\"pt_title S_txt2\\">血型：<\\/span><span class=\\"pt_detail\\">([a-zA-Z]+)<\\/span>')
b7 = patten7.findall(detail_cont)
print b7[0]
#<span class=\"pt_title S_txt2\">注册时间：<\/span>\r\n\t\t\t\t\t\t\t\t\t<span class=\"pt_detail\">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2015-09-25\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<\/span>
patten8 = re.compile(ur'<span class=\\"pt_title S_txt2\\">注册时间：<\\/span>[\\r]*[\\n]*[\\t]*<span class=\\"pt_detail\\">[\\r]*[\\n]*[\\t]*([-\d]+)[\\r]*[\\n]*[\\t]*<\\/span>')
b8 = patten8.findall(detail_cont)
print b8[0]
#
patten9 = re.compile(ur'<span class=\\"pt_title S_txt2\\">注册时间：<\\/span>[\\r]*[\\n]*[\\t]*<span class=\\"pt_detail\\">[\\r]*[\\n]*[\\t]*([-\d]+)[\\r]*[\\n]*[\\t]*<\\/span>')
b9 = patten9.findall(detail_cont)
print b9[0]

