#coding:utf8
'''
Created on 2016年4月20日

@author: wb-zhaohaibo
'''

import MySQLdb
print MySQLdb

conn = MySQLdb.Connect(
                       host="127.0.0.1",
                       port=3306,
                       user="root",
                       passwd="admin",
                       db="testsql",
                       charset="utf8"
                       )
cursor = conn.cursor()

sql = "select * from student"
cursor.execute(sql)
rs = cursor.fetchall()
for row in rs:
    print "userid: %d , username:%s" % row

cursor.close()
conn.close()



