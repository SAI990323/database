import pymysql.cursors
import os

class Mysql:
    def __init__(self):
        pymysql.connect()
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db = 'dbname',
            charset='UTF8MB4'
        )
        self.load()

    def load(self):
        self.executeScriptsFromFile('DDL+drop.sql')
        self.executeScriptsFromFile('largeRelationsInsertFile.sql')
        self.connection.commit()

    def delete(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        cursor.close()

    def insert(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        cursor.close()

    def query(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        colname = []
        colinfo = []
        for col in cursor.description:
            colname.append(col[0])
        for da in data:
            li = []
            for i in da:
                li.append(i)
            colinfo.append(li)
        cursor.close()
        return colname, colinfo

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def close(self):
        self.connection.close()

    def create_view(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        cursor.close()
        self.commit()

    def executeScriptsFromFile(self,filename):
        fd = open(filename, 'r', encoding='utf-8')
        cursor = self.connection.cursor()
        sqlfile = fd.read()
        fd.close()
        sqlcommands = sqlfile.split(';')
        for command in sqlcommands:
            try:
                cursor.execute(command)
            except Exception as msg:
                print(msg)
        cursor.close()
        print('sql执行完成')

