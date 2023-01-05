# encoding=utf-8
import pymysql

config = {
          'host': '120.78.173.82',#'localhost'
          'port': 3306,     #MySQL默认端口
          'user': 'root',    #mysql默认用户名
          'password': 'K1qOHvbSmqbe4XNwz1Nj',
          'database': 'bms',  #数据库
          'charset': 'utf8mb4',
          'cursorclass': pymysql.cursors.DictCursor,
}
