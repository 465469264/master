# encoding=utf-8
import pymysql

config = {
          'host': '10.0.2.17',#'localhost'
          'port': 3306,     #MySQL默认端口
          'user': 'dev',    #mysql默认用户名
          'password': 'T3sbPtjYElXrjHJs5i9c',
          'database': 'bms',  #数据库
          'charset': 'utf8mb4',
          'cursorclass': pymysql.cursors.DictCursor,
}
