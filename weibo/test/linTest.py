# coding:utf8
'''
Created on 2016年4月19日

@author: wb-zhaohaibo
'''
import re

st = "<http>我说的<a><http>是等丰富的<a>这里是中文_".decode("utf8")
pattenst = re.compile(ur'[<>\w\u4e00-\u9fa5]+([\u4e00-\u9fa5]+)_')
cs = pattenst.findall(st)
print cs
print cs[0]