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

sql_insert = "insert into student(userid,username) values(11,'赵海博')"
sql_update = "update student set username = '测试01' where userid = 8"
sql_delete = "delete from student where userid < 3"

try:
    #MySQLdb默认关闭事务自动提交
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount
    #事务提交
    conn.commit()
except Exception as e:
    print e
    #事务回滚
    conn.rollback()   

cursor.close()
conn.close()



