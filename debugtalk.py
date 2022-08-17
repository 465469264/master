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

'''hr
app>har2case apply.har
hrun -s apply.json


'''


def get_httprunner_version():
    return __version__
def sum_two(m, n):
    return m + n
def sleep(n_secs):
    time.sleep(n_secs)

#APP的
# 校验学员+老师身份消息通知title
def judge_newUnReadNum(newUnReadNum7,newUnReadNum9):
    try:
        assert int(newUnReadNum7) == 1
        log.info("newUnReadNum新消息正确")
    except AssertionError:
        log.error("newUnReadNum新消息错误")

#校验首页小鸡的新消息数据数量
def judge_newUnReadNum2(ls,unReadMsgNum):
    print(ls)
    for a in range(len(ls)):
        if ls[a] == None:
            ls[a] = 0
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

# 判断报名活动的消息推送
def selAppMsgCenter_msgtype2(body):
    try:
        assert "恭喜你成功报名" in str(body["body"][4]["newMsg"])
        log.info("报名活动消息推送成功")
    except AssertionError:
        log.error("报名活动消息推送错误")

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

#判断是否已登录
def judge_sing(body):
    if body == True:
        return "您今天已经签过到啦~"
    elif body == False:
        return "success"

#判断智米奖励是否已领取
def ifReceive(body):
    if body == 1:
        return "该等级的奖励已领取"
    elif body == False:
        return "success"

#判断学籍
def judge_learnId(learnId,learnId1,learnId_dangqian):
    if learnId_dangqian == learnId:
        a = learnId1
        return a
    elif learnId_dangqian == learnId1:
        a = learnId
        return a




# 公用模块
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

#延迟执行
def delay(body):
    time.sleep(body)

#获取当前时间
def now_times():
    return(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

#获取当前时间后一个小时
def time_late():
    return((datetime.datetime.now() + datetime.timedelta(hours=+1)).strftime("%Y/%m/%d %H:%M:%S"))

# 往后1分钟
def time_late_minutes():
    return ((datetime.datetime.now() + datetime.timedelta(minutes=+5)).strftime("%Y/%m/%d %H:%M:%S"))

# 获取往后6天时间
def day_late():
    return ((datetime.datetime.now() + datetime.timedelta(days=6)).strftime("%Y/%m/%d %H:%M:%S"))


# 写入测试数据，及读取测试数据
# 全局搜索指定文件夹路径
def search_file(a):
    f_list = [os.path.dirname(os.path.abspath(__file__))]   #获取项目路径
    f_str = a
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

# 读取data的测试数据
def read_data_number(a,b):
    c = search_file('data.ini')
    ini_path = c
    config = configparser.ConfigParser()
    config.read(ini_path,encoding="utf-8-sig")
    print(config.get(a,b))
    return config.get(a,b)

#把APP手机号注册参数写入到data文件
def w_env(mobile):
    """
    更新后台的authtoken，减少登录操作
    :param authtoken:
    :return:
    """
    a = search_file('.env')
    # file_dir = os.path.abspath('../..')  # 获取上级路径
    # file_dir = os.path.abspath(os.path.join(os.getcwd(), "../.."))  # 获取上上级路径
    dot_env = load_dot_env_file(a)
    dot_env.update({'register_mobile': mobile})
    with open(a, "w") as f:
        for k, v in dot_env.items():
            k_v = k + '=' + str(v)
            f.write(k_v)
            f.write('\n')

#写入app_auth_token至env
def w_env_token(app_auth_token):
    a = search_file('.env')
    dot_env = load_dot_env_file(a)
    dot_env.update({'app_auth_token': app_auth_token})
    with open(a, "w") as f:
        for k, v in dot_env.items():
            k_v = k + '=' + str(v)
            f.write(k_v)
            f.write('\n')




# 写入注册后的手机号码
def write_Register_mobile(b,mobile):
    a = search_file('data.ini')
    ini_path = a
    config = configparser.ConfigParser()
    config.read(ini_path,encoding="utf-8-sig")
    for sections in config.sections():
        for items in config.items(sections):
            print(items)
            # 如果为空则添加
            if(config.get("test_data",b)==None or config.get("test_data",b).strip()==None):
               config.set("test_data",b,mobile)
            else: #删除再添加
                config.remove_option("test_data", b)
                config.set("test_data", b,mobile)
        config.write(open(ini_path, "w+", encoding='utf-8'))




#web后台模块
# 登录web
def login_web():
    s = requests.Session()
    data = {"isOpenImage": "",
            "mobile": "18221823862",
            "ImgValidCode": "",
            "validCode": "888888"}
    url = "http://27-bms.yzwill.cn/loginByMobile.do"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "uri": "http://27-bms.yzwill.cn/toLogin.do",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    res = s.post(url=url, headers=headers, data=data)
    print(res)
    cookie = requests.utils.dict_from_cookiejar(res.cookies)["SESSION"]
    Cookie = "SESSION=" + cookie
    return Cookie

#获取web_token
def get_html(body):
    pattern = re.compile(r'value="(.+)" name="_web_token"')  # 查找数字
    body = str(body, encoding="utf-8")
    a = pattern.findall(body)
    print(type(a))
    return a[0]

# 拼接webcookie
def web_cookie(cookie):
    Cookie = "SESSION=" + str(cookie)
    return Cookie



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
def delete_task_habit(userId):
    sql = 'delete from mkt.mkt_mark_task_enroll where user_id = "{}"'.format(userId)
    data = conn_sql().get_data(sql)
    return data

# 查询用户的智米
def find_zhimi(userId):
    sql = 'SELECT zhimi_amount FROM us.us_base_info WHERE user_id = "{}"'.format(userId)
    data = conn_sql().get_data(sql)
    return data

#缴费单
def feeList():
    feeList=[{"itemCode":"Y1","itemName":"代收第一年学费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"2","itemYear":"1","itemType":"2","feeId":None,"itemSeq":None},{"itemCode":"S1","itemName":"代收第一年书费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"3","itemYear":"1","itemType":"4","feeId":None,"itemSeq":None},{"itemCode":"Y2","itemName":"代收第二年学费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"5","itemYear":"2","itemType":"2","feeId":None,"itemSeq":None},{"itemCode":"S2","itemName":"代收第二年书费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"6","itemYear":"2","itemType":"4","feeId":None,"itemSeq":None},{"itemCode":"Y3","itemName":"代收第三年学费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"8","itemYear":"3","itemType":"2","feeId":None,"itemSeq":None},{"itemCode":"S3","itemName":"代收第三年书费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"9","itemYear":"3","itemType":"4","feeId":None,"itemSeq":None},{"itemCode":"YS","itemName":"代收艺术加考费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"100","itemYear":"1","itemType":"3","feeId":None,"itemSeq":None},{"itemCode":"Y0","itemName":"考前辅导费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"103","itemYear":"0","itemType":"1","feeId":None,"itemSeq":None}]
    return feeList

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

# 修改习惯打卡任务
def update_task(id1,id2):
    a = now_times()
    b = day_late()
    c = time_late_minutes()
    sql = 'UPDATE mkt.bd_mark_task_info SET enroll_end_time = "{}",start_time = "{}",end_time = "{}",divide_reward_time = "{}",status = 2 where id = "{}"'.format(c,a,b,b,id1)
    sql2 = 'UPDATE mkt.bd_mark_task_info SET enroll_end_time = "{}",start_time = "{}",end_time = "{}",divide_reward_time = "{}",status = 2 where id = "{}"'.format(c,a,b,b,id2)
    data1 = conn_sql().get_data(sql)
    data2 = conn_sql().get_data(sql2)
    return data1,data2


#查询最新的一次我的上进分明细
def find_MyScoreInfos(userId):
    sql = 'SELECT behavior_desc FROM mkt.gs_score_change_record where user_id = "{}" ORDER BY create_time desc limit 1'.format(userId)
    data = conn_sql().get_data(sql)[0]['behavior_desc']
    print(data)
    return data

#根据学服任务id,修改数据库中这个学服任务的id为未读
def student_task(taskId):
    sql = 'UPDATE bms.oa_student_task SET is_read = 0 where task_id = "{}"'.format(taskId)
    data = conn_sql().get_data(sql)
    print(data)
    return data


#直播间相关sql
#删除直播间管理员垃圾数据
def delete_lives_admin(mobile):
    sql = 'delete from bms.bd_lives_admin where mobile = "{}"'.format(mobile)
    data = conn_sql().get_data(sql)
    return data

#修改让腾讯云直播开播
def Modify_lives_schedule(id):
    a = now_times()
    b = time_late()
    sql = 'UPDATE bms.bd_lives_schedule SET start_time ="{}",end_time = "{}",status = 1 where id="{}"'.format(a,b,id)
    data = conn_sql().get_data(sql)


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






#测试用例传参
#发票类
def Apply_record():
    return [
        {"title":"企业发票-正常传参","companyTaxNumber": "123456789111111111", "invoiceTitle": "1", "companyName": "测试", "applyPurpose": "测试","email": "123@qq.com","message": "success",},
        {"title":"企业发票-税号为空","companyTaxNumber": "", "invoiceTitle": "1", "companyName": "测试", "applyPurpose": "测试","email": "123@qq.com","message": "success",},
        {"title":"企业发票-邮箱为空","companyTaxNumber": "123456789111111111", "invoiceTitle": "1", "companyName": "测试", "applyPurpose": "测试", "email": "123@qq.com","message": "success",},
        {"title":"企业发票-税号邮箱为空","companyTaxNumber": "", "invoiceTitle": "1", "companyName": "测试", "applyPurpose": "测试","email": "","message": "success",},
        {"title": "企业发票-公司名称为空", "companyTaxNumber": "123456789111111111", "invoiceTitle": "1", "companyName": "", "applyPurpose": "测试","email": "123@qq.com","message": "success",},
        {"title": "企业发票-申请说明为空", "companyTaxNumber": "123456789111111111", "invoiceTitle": "1", "companyName": "","applyPurpose": "", "email": "123@qq.com","message": "success",},
        {"title": "个人发票-正常传参", "companyTaxNumber": "", "invoiceTitle": "2", "companyName": "","applyPurpose": "测试", "email": "123@qq.com","message": "success",},
        {"title": "个人发票-传税号及公司名称", "companyTaxNumber": "123456789111111111", "invoiceTitle": "2", "companyName": "测试","applyPurpose": "测试", "email": "123@qq.com","message": "success",},
        {"title": "个人发票-申请说明，邮箱传空", "companyTaxNumber": "", "invoiceTitle": "2", "companyName": "","applyPurpose": "", "email": "","message": "success",},

    ]

#报读证明
def Apply_Enrollment():
    return[
        {"title":"正常传参","remark": "测试","applyPurpose": "测试","message": "success",},
        {"title":"备注为空","remark": "","applyPurpose": "测试","message": "success"},
        {"title":"申请理由为空","remark": "测试","applyPurpose": "","message": "success"},
        {"title": "备注/申请理由为空", "remark": "", "applyPurpose": "","message": "success"},
        {"title":"申请理由及备注的输入类型","remark": "测@123风fF","applyPurpose": "测@123风fF","message": "success"}

    ]

# 评论活动
def Activity_content():
    return [
        {"title": "传1个字符", "content": "a", "message": "success"},
        {"title":"评论传空","content":"","message":"评论的内容与图片不能同时为空"},
        {"title":"正常传参","content":"测试测试测试","message":"success"},
        {"title":"参数超长","content":"热评外显，默认取动态中点赞最高评论放在外面显示，只显示一条；且评论的点赞数要达到>>5个赞才显示在列表外如果某条动态热评最高的点赞只有4个赞，则这条热评不外显在列表外,动态详情的评论增加按热度的排序，默认按热度排序,按热度排：点赞从","message":"success"},
        {"title":"参数类型传参","content":"@@123haha  --22","message":"success"},
    ]

#跑步打卡数据
def run():
    return[
        {"distance":"3","spendDesc":"9'19","runSecond":"0.47","historyRun":"0","runTime":"00:27:59"}
    ]

#搜索接口不同类型及不同关键字
def search():
    # 类型，0>搜索栏搜索    6>上进学社   2>查询好友  7>查询老师  4>上进习惯  5>上进活动  3>查看话题  1>查看动态  8>礼品商城  12>上进直播
    return[
        {"title": "关键字传空", "keyWords": "", "type": "2", "message": "success"},
        {"title": "type传空", "keyWords": "a", "type": "", "message": "服务网络有异常，请稍候再试！"},
        {"title":"搜索全部","keyWords": "a","type": "0","message": "服务网络有异常，请稍候再试！"},
        {"title":"搜索好友","keyWords": "测试测试测试", "type": "2","message": "success"},
        {"title":"搜索话题","keyWords": "测试", "type": "3","message": "success"},
        {"title":"搜索上进习惯","keyWords": "amylee", "type": "4","message": "success"},
        {"title":"搜索上进活动","keyWords": "a", "type": "5","message": "success"},
        {"title":"搜索上进学社","keyWords": "测", "type": "6","message": "success"},
        {"title":"搜索礼品商城","keyWords": "amylee", "type": "8","message": "success"},
    ]

#优惠券传值，分别查所有优惠券，查报读的优惠政策，非报读的优惠政策
def Coupons_scholarship():
    return[
        {"title":"都不传","recruitType": "","scholarship": "","message": "success",},
        {"title":"传其他的优惠政策","recruitType": "1","scholarship": "1273","message": "success",},
        {"title":"scholarship","recruitType": "","scholarship": "1272","message": "success",}
    ]

#我的页面-帮助与反馈>传值
def channel():
    return[
        {"title":"问题1","channel": "1", "message": "success"},
        {"title":"问题3","channel": "3", "message": "success"},
        {"title":"问题5","channel": "5", "message": "success"},
        {"title":"问题6","channel": "6", "message": "success"},
        {"title":"问题1，3，5，6","channel": "1,3,5,6", "message": "success"},
        {"title": "channel传空", "channel": "", "message": "服务网络有异常，请稍候再试！"},

    ]

#消息通知一键已读
def msgType():
    return[
        {"msgType":"1"},{"msgType":"1"},{"msgType":"2"},{"msgType":"3"},{"msgType":"4"},{"msgType":"5"},{"msgType":"6"},{"msgType":"7"},{"msgType":"8"},{"msgType":"9"},{"msgType":"10"},

    ]

#智米商城列表对应的商品类型
def salesType_goodsType():
    return [
        {"title":"正常传参","salesType": "1","goodsType": "1","message":"success"},
        {"title":"活动类型传空","salesType": "", "goodsType": "2", "message": "success"},
        {"title":"商品类型传空","salesType": "1", "goodsType": "", "message": "success"},
        {"title":"活动/商品穿孔","salesType": "", "goodsType": "", "message": "success"},

    ]
