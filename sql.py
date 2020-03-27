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
        self.cursor = self.connection.cursor()
        self.load()

    def load(self):
        self.executeScriptsFromFile('DDL+drop.sql')
        self.executeScriptsFromFile('largeRelationsInsertFile.sql')
        self.connection.commit()

    def delete(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def query(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        data = self.cursor.fetchall()
        print(data)

    def close(self):
        self.connection.close()

    def executeScriptsFromFile(self,filename):
        fd = open(filename, 'r', encoding='utf-8')
        sqlfile = fd.read()
        fd.close()
        sqlcommands = sqlfile.split(';')
        for command in sqlcommands:
            try:
                self.cursor.execute(command)
            except Exception as msg:
                print(msg)
        print('sql执行完成')

