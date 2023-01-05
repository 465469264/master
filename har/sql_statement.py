# encoding=utf-8
import pymysql
from pymysql import ProgrammingError
class conn_sql():
    def __init__(self):
        self.database= "bms"
        self.user= "root"
        self.password= "K1qOHvbSmqbe4XNwz1Nj"
        self.host="120.78.173.82"
        self.port= 3306
        self.cursorclass = pymysql.cursors.DictCursor

    def get_data(self, sql):
        data = None
        conn = pymysql.connect(database = self.database,user =self.user,password =self.password,host = self.host,port =  self.port,cursorclass=self.cursorclass)
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
        except TypeError:
            cursor.executemany(sql)
        except ProgrammingError:
            return 'sql语句有误'
        # 如果sql语句以SELECT开头
        if sql.upper().startswith('SELECT'):
            # 获取查询的结果
            data = cursor.fetchall()
        else:
            print('更新了数据')
            conn.commit()  # 提交sql语句
        # 关闭数据库连接
        conn.close()
        return data

