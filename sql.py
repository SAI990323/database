import pymysql.cursors


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

    def delete(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def query(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
