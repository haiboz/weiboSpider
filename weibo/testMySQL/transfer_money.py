#coding:utf8
'''
Created on 2016年4月20日

@author: wb-zhaohaibo
'''
import sys
import MySQLdb


class TransferMoney(object):
    #银行转账操作流程
    
    def __init__(self, conn):
        self.conn = conn
    
    def check_acct_available(self, acctid):
        '''检查账户 有效性'''
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid = %s" % acctid
            cursor.execute(sql)
            print "check_acct_sql:%s" % sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise "账号不存在： %s" % acctid
        except Exception as e:
            raise e
            cursor.close()
    
    
    def check_enougn_money(self, acctid, money):
        '''检测是否有足够的钱"'''
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid = %s and money >= %s " % (acctid,money)
            cursor.execute(sql)
            print "check_money_sql:%s" % sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise "账号没有足够的钱： %s" % acctid
        except Exception as e:
            raise e
            cursor.close()
    
    
    def reduce(self, acctid, money):
        '''金额减操作'''
        cursor = self.conn.cursor()
        try:
            sql = "update account set money = money - %s where acctid = %s" % (money,acctid)
            cursor.execute(sql)
            print "reduce_sql:%s" % sql
            if cursor.rowcount != 1L:
                raise "金额减操作异常： %s" % acctid
        except Exception as e:
            raise e
            cursor.close()
    
    
    def add(self, acctid, money):
        '''金额减操作'''
        cursor = self.conn.cursor()
        try:
            sql = "update account set money = money + %s where acctid = %s" % (money,acctid)
            cursor.execute(sql)
            print "add_sql:%s" % sql
            if cursor.rowcount != 1L:
                raise "金额加操作异常： %s" % acctid
        except Exception as e:
            raise e
            cursor.close()
    
    
    def transfer(self, source_acctid, target_acctid, money):
        try:
            #检测账号是否可用
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            #检测是否有足够的钱
            self.check_enougn_money(source_acctid,money)
            #原账户减去金额
            self.reduce(source_acctid,money)
            #目标账户加上金额
            self.add(target_acctid,money)
            #提交事务
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            #抛出异常
            raise e
    
        
if __name__ == "__main__":
    source_acctid = 1#sys.argv[1]
    target_acctid = 2#sys.argv[2]
    money = 10#sys.argv[3]
    
    conn = MySQLdb.Connect(
                           host="127.0.0.1",
                           port=3306,
                           user="root",
                           passwd="admin",
                           db="testsql",
                           charset="utf8"
                           )
    transfer_money = TransferMoney(conn)
    
    try:
        transfer_money.transfer(source_acctid,target_acctid,money)
    except Exception as e:
        print "出现异常："+ str(e)
    finally:
        conn.close()
