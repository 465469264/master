import time,base64,random,requests,json,datetime
import uuid

from faker import Faker
from httprunner import __version__
from httprunner.loader import load_dot_env_file
from har.sql_statement import conn_sql
from har.logger import log
import configparser,os,yaml
f = Faker(locale='zh_CN')
import re,oss2

'''
app>har2case apply.har
hrun -s apply.json


'''


def get_httprunner_version():
    return __version__
def sum_two(m, n):
    return m + n
def sleep(n_secs):
    time.sleep(n_secs)

#公共模块
# 校验学员+老师身份消息通知title
def judge_newUnReadNum(newUnReadNum7,newUnReadNum9):
    try:
        assert int(newUnReadNum7) == 1
        assert int(newUnReadNum9) == 1
        log.info("newUnReadNum新消息正确")
    except AssertionError:
        log.error("newUnReadNum新消息错误")

#校验首页小鸡的新消息数据数量
def judge_newUnReadNum2(ls,unReadMsgNum):
    print(ls)
    for a in range(len(ls)):
        if ls[a] == None:
            ls[a] = 0
    # print(ls)
    # print(sum(ls))
    # return sum(ls)
    try:
        assert sum(ls) == unReadMsgNum
        log.info("首页小鸡的新消息新消息正确")
    except AssertionError:
        log.error("首页小鸡的新消息新消息错误")

# 判断老师身份账号登录默认带出跑步绩效话题+X月累计打卡X天（X月是指本月，X天是累计X天发帖，1天内不管发多少次算1天）
def judge_topic1(body):
    try:
        assert body['topicName'] == "#上进远智跑团打卡#"
        log.info("跑步绩效话题正确")
    except AssertionError:
        log.error("跑步绩效话题错误")

# 老师+习惯：默认带出跑步绩效话题+跑步习惯话题+习惯自动话术
def judge_topic2(body):
    try:
        assert body['topicName'] == "#amylee跑步测试勿删#,#上进远智跑团打卡#"
        assert body['taskName'] == "amylee跑步测试勿删"
        log.info("跑步绩效话题正确")
    except AssertionError:
        log.error("跑步绩效话题错误")

# 其他用户+习惯，默认带出习惯话题+习惯自动话术
def judge_topic3(body):
    try:
        assert body['topicName'] == "#amylee跑步测试勿删#"
        assert body['taskName'] == "amylee跑步测试勿删"
        log.info("跑步绩效话题正确")
    except AssertionError:
        log.error("跑步绩效话题错误")

#老师+习惯：默认带出读书绩效话题+读书习惯话题+习惯自动话术
def judge_topic4(body):
    try:
        assert body['topicName'] == "#amylee读书打卡勿删测试#,#上进远智读书会打卡#"
        assert body['taskName'] == "amylee读书打卡勿删测试"
        log.info("读书绩效话题正确")
    except AssertionError:
        log.error("读书绩效话题错误")

# 老师：默认带出读书绩效话题+X月累计打卡X次
def judge_topic5(body):
    try:
        assert "累计" in body['markContent']
        assert body['topicName'] == "#上进远智读书会打卡#"
        log.info("读书绩效话题正确")
    except AssertionError:
        log.error("读书绩效话题错误")

# 判断报名活动的消息推送
def selAppMsgCenter_msgtype2(body):
    try:
        assert "恭喜你成功报名" in str(body["body"][4]["newMsg"])
        log.info("报名活动消息推送成功")
    except AssertionError:
        log.error("报名活动消息推送错误")



# 接口数据加密
def base64_encode(code):
    data = base64.b64encode(str(code).encode()).decode()
    # print(data)
    return data

# 获取随机手机号码
def get_mobile():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
               "155", "156", "157", "158", "159", "186", "187", "188"]
    return str(random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8)))

# 获取未注册的随机手机号码
def get_not_exist_mobile():
    while True:
        mobile = get_mobile()
        data = {"mobile": mobile}
        response = requests.post("http://bms.yzwill.cn/recruit/getStudentInfoByMobile", data=data)
        result = response.text
        if result == '{"code":"00","body":null,"msg":"","ok":true}':
            return mobile
        else:
            continue

# 随机生成姓名
def get_name():
    """随机生成姓名"""
    return f.name()

# 生成身份证
def idcard():
    """生成身份证"""
    return f.ssn()

#获取ini文件路径
def search_data_ini():
    f_list = [os.path.dirname(os.path.abspath(__file__))]   #获取项目路径
    f_str = 'data.ini'
    s_list = f_list.copy()
    f_list.clear()
    for x_dir in s_list:
        if os.path.isdir(x_dir):
            try:
                for fname in os.listdir(x_dir):
                    fpath = os.path.join(x_dir, fname)
                    if f_str in fname and os.path.isfile(fpath):
                        return fpath
                    elif os.path.isdir(fpath):
                        # 保存下一级目录
                        f_list.append(fpath)
            except IOError:
                print("错的", x_dir)

#全局搜索指定文件夹路径
def search_file():
    f_list = [os.path.dirname(os.path.abspath(__file__))]  #获取项目路径
    f_str = '.env'
    s_list = f_list.copy()
    f_list.clear()
    for x_dir in s_list:
        if os.path.isdir(x_dir):
            try:
                for fname in os.listdir(x_dir):
                    fpath = os.path.join(x_dir, fname)
                    if f_str in fname and os.path.isfile(fpath):
                        return fpath
                    elif os.path.isdir(fpath):
                        # 保存下一级目录
                        f_list.append(fpath)
            except IOError:
                print("错的", x_dir)

#获取当前时间
def now_times():
    return(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

#获取当前时间后一个小时
def time_late():
    return((datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%Y/%m/%d %H:%M:%S"))

def time_late_minutes():
    return ((datetime.datetime.now() + datetime.timedelta(minutes=+1)).strftime("%Y/%m/%d %H:%M:%S"))

# 获取往后6天时间
def day_late():
    return ((datetime.datetime.now() + datetime.timedelta(days=6)).strftime("%Y/%m/%d %H:%M:%S"))


#延迟执行
def delay(body):
    time.sleep(body)


#web后台模块
#缴费单
def feeList():
    feeList=[{"itemCode":"Y1","itemName":"代收第一年学费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"2","itemYear":"1","itemType":"2","feeId":None,"itemSeq":None},{"itemCode":"S1","itemName":"代收第一年书费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"3","itemYear":"1","itemType":"4","feeId":None,"itemSeq":None},{"itemCode":"Y2","itemName":"代收第二年学费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"5","itemYear":"2","itemType":"2","feeId":None,"itemSeq":None},{"itemCode":"S2","itemName":"代收第二年书费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"6","itemYear":"2","itemType":"4","feeId":None,"itemSeq":None},{"itemCode":"Y3","itemName":"代收第三年学费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"8","itemYear":"3","itemType":"2","feeId":None,"itemSeq":None},{"itemCode":"S3","itemName":"代收第三年书费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"9","itemYear":"3","itemType":"4","feeId":None,"itemSeq":None},{"itemCode":"YS","itemName":"代收艺术加考费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"100","itemYear":"1","itemType":"3","feeId":None,"itemSeq":None},{"itemCode":"Y0","itemName":"考前辅导费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"103","itemYear":"0","itemType":"1","feeId":None,"itemSeq":None}]
    return feeList

#获取web_token
def get_html(body):
    pattern = re.compile(r'value="(.+)" name="_web_token"')  # 查找数字
    body = str(body, encoding="utf-8")
    a = pattern.findall(body)
    print(type(a))
    return a[0]

#27环境执行生成学院订单
def College_order(learn_Id):
    sql = 'INSERT INTO pay.bd_sub_order (sub_order_no,order_no,item_code,item_name,item_seq,item_year,item_type,fee_amount,offer_amount,payable,sub_order_status,std_id,std_name,mobile,id_card,user_id,sub_learn_id ) SELECT bms.seq (),' \
          'CONCAT( "YZ", DATE_FORMAT( NOW(), "%Y%m%d%H%i%s" ), "12378"),it.item_code,it.item_name,it.delay_num,it.item_year,it.item_type,f.define_amount,0.00,f.define_amount,"1",li.std_id,li.ln_std_name,li.mobile,li.id_card,si.user_id,' \
          'li.learn_id FROM bms.bd_fee_define f LEFT JOIN bms.bd_learn_info li ON li.fee_id = f.fee_id LEFT JOIN bms.bd_fee_item it ON it.item_code = f.item_code LEFT JOIN bms.bd_student_info si ON si.std_id = li.std_id WHERE li.learn_id = "{}"'.format(learn_Id)
    data = conn_sql().get_data(sql)
    return data
# College_order('164880778923176371')

#27环境执行删除生成多的最后两条订单
def delete_order(learnId):
    sql = 'delete from pay.bd_sub_order where sub_order_no in (select t.sub_order_no from (select * from pay.bd_sub_order where sub_learn_id = "{}" order by sub_order_no desc limit 0,2)as t)'.format(learnId)
    data = conn_sql().get_data(sql)
    return data

# 拼接webcookie
def web_cookie(cookie):
    Cookie = "SESSION=" + str(cookie)
    return Cookie


# app模块
# 读取data的测试数据
def read_data_number(a,b):
    c = search_data_ini()
    ini_path = c
    config = configparser.ConfigParser()
    config.read(ini_path,encoding="utf-8-sig")
    print(config.get(a,b))
    return config.get(a,b)



#把APP手机号注册参数写入到env文件
def w_env(mobile):
    """
    更新后台的authtoken，减少登录操作
    :param authtoken:
    :return:
    """
    a = search_file()
    # file_dir = os.path.abspath('../..')  # 获取上级路径
    # file_dir = os.path.abspath(os.path.join(os.getcwd(), "../.."))  # 获取上上级路径
    dot_env = load_dot_env_file(a)
    dot_env.update({'register_mobile': mobile})
    with open(a, "w") as f:
        for k, v in dot_env.items():
            k_v = k + '=' + str(v)
            f.write(k_v)
            f.write('\n')


# 写入注册后的手机号码
def write_Register_mobile(mobile):
    a = search_data_ini()
    ini_path = a
    config = configparser.ConfigParser()
    config.read(ini_path,encoding="utf-8-sig")
    for sections in config.sections():
        for items in config.items(sections):
            print(items)
            # 如果为空则添加
            if(config.get("test_data","Register_mobile")==None or config.get("test_data","Register_mobile").strip()==None):
               config.set("test_data", "Register_mobile",mobile)
            else: #删除再添加
                config.remove_option("test_data", "Register_mobile")
                config.set("test_data", "Register_mobile",mobile)
        config.write(open(ini_path, "w+", encoding='utf-8'))


# 修改数据库模块
# 修改优惠券的开始结束时间
def coupon(coupon_id):
    a = now_times()
    b = time_late()
    sql = 'UPDATE bms.bd_coupon SET publish_start_time ="{}",publish_expire_time = "{}" where coupon_id= "{}"'.format(a,b,coupon_id)
    data = conn_sql().get_data(sql)

#把学员变为在线学员
def std_stage(learnId):
    sql = 'UPDATE `bms`.`bd_learn_info` SET std_stage=7 WHERE learn_id ={}'.format(learnId)
    data = conn_sql().get_data(sql)
    return data

#修改数据库的开播时间和开播状态
def Modify_lives_schedule():
    a = now_times()
    b = time_late()
    sql = 'UPDATE bms.bd_lives_schedule SET start_time ="{}",end_time = "{}",status = 1 where id=254'.format(a,b)
    data = conn_sql().get_data(sql)
    # return data

#修改数据库让直播类型为营销课
def Marketing_class_yingxiao():
    a = now_times()
    b = time_late()
    sql = 'UPDATE bms.bd_lives_schedule SET start_time ="{}",end_time = "{}",status = 1,live_type =3 where id=254'.format(a, b)
    data = conn_sql().get_data(sql)
    return data

#修改数据库让直播类型为公开课 哼哼哈嘿的id是254
def Marketing_class_gongkai():
    a = now_times()
    b = time_late()
    sql = 'UPDATE bms.bd_lives_schedule SET start_time ="{}",end_time = "{}",status = 1,live_type =1 where id=254'.format(a, b)
    data = conn_sql().get_data(sql)
    return data

# 修改活动为未提醒
def update_activity():
    sql = 'UPDATE mkt.mkt_upward_activity SET is_send=0 WHERE id=206'
    data = conn_sql().get_data(sql)
    return data

# 删除用户的报名活动记录
def delete_activity(a):
    sql = 'delete from mkt.mkt_upward_enroll where user_id = "{}"'.format(a)
    data = conn_sql().get_data(sql)
    return data

# 删除用户的习惯打卡报名记录
# def delete_task_habit(userId):
#     sql = 'delete from mkt.mkt_mark_task_enroll where user_id = "{}"'.format(userId)
#     data = conn_sql().get_data(sql)
#     return data


# 修改打卡任务
def update_task():
    a = now_times()
    b = day_late()
    c = time_late_minutes()
    sql = 'UPDATE mkt.bd_mark_task_info SET enroll_end_time = "{}",start_time = "{}",end_time = "{}",divide_reward_time = "{}",status = 2 where id = 905'.format(c,a,b,b)
    sql2 = 'UPDATE mkt.bd_mark_task_info SET enroll_end_time = "{}",start_time = "{}",end_time = "{}",divide_reward_time = "{}",status = 2 where id = 906'.format(c,a,b,b)
    sql3 = 'UPDATE mkt.bd_mark_task_info SET enroll_end_time = "{}",start_time = "{}",end_time = "{}",divide_reward_time = "{}",status = 2 where id = 907'.format(c,a,b,b)
    sql4 = 'UPDATE mkt.bd_mark_task_info SET enroll_end_time = "{}",start_time = "{}",end_time = "{}",divide_reward_time = "{}",status = 2 where id = 908'.format(c,a,b,b)
    data1 = conn_sql().get_data(sql)
    data2 = conn_sql().get_data(sql2)
    data3 = conn_sql().get_data(sql3)
    data4 = conn_sql().get_data(sql4)
    return data1,data2,data3,data4



# 获取图片上传路径
def upload(accessKeyId,accessKeySecret,endpoint,localFile,bucketName):
    auth = oss2.Auth(accessKeyId, accessKeySecret)
    bucket = oss2.Bucket(auth, endpoint, bucketName)
    s_uuid = str(uuid.uuid4())
    l_uuid = s_uuid.split('-')
    uid = ''.join(l_uuid)
    (shotname,extension) = os.path.splitext(localFile)
    scPicUrl = uid + extension
    bucket.put_object_from_file(scPicUrl, localFile)
    return scPicUrl



