# encoding=utf-8
import pymysql
from pymysql import ProgrammingError
# def sql_run(sql, arg=None, config=None):
#     data = None
#     from har.mysql_setting import config
#     # 打开数据库连接
#     conn = pymysql.connect(**config)
#     # 使用cursor()方法创建一个游标对象
#     cursor = conn.cursor()
#     try:
#         cursor.execute(sql, arg)
#     except TypeError:
#         cursor.executemany(sql, arg)
#     except ProgrammingError:
#         return 'sql语句有误'
#     # 如果sql语句以SELECT开头
#     if sql.upper().startswith('SELECT'):
#         # 获取查询的结果
#         data = cursor.fetchall()
#     else:
#         print('更新了数据')
#         conn.commit()  # 提交sql语句
#     # 关闭数据库连接
#     conn.close()
#     return data

# data = sql_run("UPDATE bms.bd_learn_info SET std_type=1  WHERE mobile = 13729043333")
# data = sql_run("")
# if __name__ == '__main__':
#     sql = 'INSERT INTO pay.bd_sub_order (sub_order_no,order_no,item_code,item_name,item_seq,item_year,item_type,fee_amount,offer_amount,payable,sub_order_status,std_id,std_name,mobile,id_card,user_id,sub_learn_id ) SELECT bms.seq (),' \
#     'CONCAT( "YZ", DATE_FORMAT( NOW(), "%Y%m%d%H%i%s" ), "12378"),it.item_code,it.item_name,it.delay_num,it.item_year,it.item_type,f.define_amount,0.00,f.define_amount,"1",li.std_id,li.ln_std_name,li.mobile,li.id_card,si.user_id,' \
#     'li.learn_id FROM bms.bd_fee_define f LEFT JOIN bms.bd_learn_info li ON li.fee_id = f.fee_id LEFT JOIN bms.bd_fee_item it ON it.item_code = f.item_code LEFT JOIN bms.bd_student_info si ON si.std_id = li.std_id WHERE li.learn_id = "164880778923176371"'
#     data = sql_run(sql)
class conn_sql():
    def __init__(self):
        self.database= "bms"
        self.user= "dev"
        self.password= "T3sbPtjYElXrjHJs5i9c"
        self.host="10.0.2.17"
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

# sql = 'INSERT INTO pay.bd_sub_order (sub_order_no,order_no,item_code,item_name,item_seq,item_year,item_type,fee_amount,offer_amount,payable,sub_order_status,std_id,std_name,mobile,id_card,user_id,sub_learn_id ) SELECT bms.seq (),' \
# 'CONCAT( "YZ", DATE_FORMAT( NOW(), "%Y%m%d%H%i%s" ), "12378"),it.item_code,it.item_name,it.delay_num,it.item_year,it.item_type,f.define_amount,0.00,f.define_amount,"1",li.std_id,li.ln_std_name,li.mobile,li.id_card,si.user_id,' \
# 'li.learn_id FROM bms.bd_fee_define f LEFT JOIN bms.bd_learn_info li ON li.fee_id = f.fee_id LEFT JOIN bms.bd_fee_item it ON it.item_code = f.item_code LEFT JOIN bms.bd_student_info si ON si.std_id = li.std_id WHERE li.learn_id = "164880778923176371"'
# data = conn_sql().get_data(sql)

# data = conn_sql().get_data("SELECT zhimi_amount,user_id FROM us.us_base_info  WHERE mobile = '15521478896'")
