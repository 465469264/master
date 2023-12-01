import time,base64,random,requests,json,datetime,re,sys
import uuid

from faker import Faker
from httprunner import __version__
from httprunner.loader import load_dot_env_file
from har.sql_statement import conn_sql
# from har.logger import log
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

#判断用户对帖子是否已经点赞，若已点赞-则取消点赞，若没点赞-则进行点赞
def judge_fabulousNum(fabulous):
    if int(fabulous) == 1:
        fabulousNum = -1
        return fabulousNum
    elif int(fabulous) == 0:
        fabulousNum = 1
        return fabulousNum

#判断帖子的评论是否已点赞
def judge_ifFabulous(ifFabulous):
    if int(ifFabulous) == 1:
        fabulousNum_comment = -1
        return fabulousNum_comment
    elif int(ifFabulous) == 0:
        fabulousNum_comment = 1
        return fabulousNum_comment

#提取习惯的id和开始时间戳
def get_task_id(body):
    a = timestap()
    data_list = body
    taskId = [item['id'] for item in data_list if a >item['startTime']][0]
    return(taskId)

#精准定位图片位置
def find_file(file_name):
    # 获取当前脚本所在的目录
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # 在当前目录及其子目录中查找文件
    for root, dirs, files in os.walk(script_directory):
        if file_name in files:
            # 找到文件后返回绝对路径
            path = os.path.abspath(os.path.join(root, file_name))
            return path
    # 如果文件未找到，返回 None 或者适合你的默认值
    return None

from PIL import Image, ImageDraw, ImageFont
def edit_photo(file_name):
    path = find_file(file_name)
    image_path = path
    image = Image.open(image_path)
    width, height = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()  # 使用默认字体
    text = "hhh"
    text_position = ((width - draw.textsize(text, font=font)[0]) // 2, height // 2)
    text_color = (255, 255, 255)  # 文本颜色，RGB格式
    draw.text(text_position, text, font=font, fill=text_color)
    edited_image_path = path
    image.save(edited_image_path)
    image.show()


#根据评论详情，提取出自己的评论id，预防万一其他用户评论，导致提取了他人评论id
def get_comment_id(body,realName):
    data_list = body
    comment_Id = [item['commentId'] for item in data_list if  item['realName']== realName][0]
    return comment_Id

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
        response = requests.post("https://new.yzou.cn/recruit/getStudentInfoByMobile", data=data)
        result = response.text
        if result == '{"code":"00","body":null,"msg":"","ok":true}':
            return mobile
        else:
            continue


# 获取当前时间戳
def timestap():
    import time
    current_timestamp_seconds = time.time()
    # 将秒转换为毫秒
    current_timestamp_milliseconds = int(current_timestamp_seconds * 1000)
    return(current_timestamp_milliseconds)

def nowtime():
    from datetime import datetime
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time


def timestap2():
    from datetime import datetime
    timestamp_in_milliseconds = 1698768000000
    # 将毫秒数转换为秒数
    timestamp_in_seconds = timestamp_in_milliseconds / 1000
    # 转换为人类可读的日期时间
    human_readable_time = datetime.utcfromtimestamp(timestamp_in_seconds).strftime('%Y-%m-%d %H:%M:%S')
    return(human_readable_time)


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
            "mobile": "13729042582",
            "ImgValidCode": "",
            "validCode": "888888"}
    url = "http://test0-bms.yzwill.cn/loginByMobile.do"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "uri": "http://test0-bms.yzwill.cn/toLogin.do",
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

def inMessageList():
    return [
        {"title":"@我","msgType":"8","msgTitle":"有人@你哟~"},
        {"title": "点赞", "msgType": "9","msgTitle":"有人给你点赞啦！"},
        {"title": "评论", "msgType": "10","msgTitle":"有人给你评论啦！"},
        {"title": "粉丝", "msgType": "11","msgTitle":"有人默默关注你罗~"}
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
#修改平时成绩
def chengji():
    return[
        {"title":"用例1----常规课程卷面分整数","score":"50","rewardScore":"20","examStatus":"4","courseScoreType": "1"},
        {"title": "用例2----常规课程卷面分一位小数", "score": "20.5", "rewardScore": "20", "examStatus": "4", "courseScoreType": "1"},
        {"title": "用例3----常规课程卷面分2位小数", "score": "20.55", "rewardScore": "20", "examStatus": "4", "courseScoreType": "1"},
        {"title": "用例4----常规课程卷面分为空", "score": "", "rewardScore": "20", "examStatus": "4","courseScoreType": "1"},
        {"title": "用例5----常规课程卷面分为空,奖励分为空", "score": "", "rewardScore": "", "examStatus": "4", "courseScoreType": "1"},
        {"title": "用例6----常规课程奖励分为一位小数", "score": "", "rewardScore": "20.5", "examStatus": "4", "courseScoreType": "1"},
        {"title": "用例7----常规课程奖励分为一位小数", "score": "", "rewardScore": "20.55", "examStatus": "4", "courseScoreType": "1"},
        {"title": "用例8----常规课程奖励分为一位小数", "score": "", "rewardScore": "20.55", "examStatus": "4", "courseScoreType": "1"},
        {"title":"用例9----常规课程卷面分整数，补考状态","score":"50","rewardScore":"20","examStatus":"1","courseScoreType": "1"},
        {"title": "用例10----常规课程卷面分整数，缓考状态", "score": "50", "rewardScore": "20", "examStatus": "2", "courseScoreType": "1"},
        {"title": "用例11----常规课程卷面分整数，作弊状态", "score": "50", "rewardScore": "20", "examStatus": "5","courseScoreType": "1"},
        {"title": "用例12----常规课程卷面分整数，状态传空", "score": "50", "rewardScore": "20", "examStatus": "","courseScoreType": "1"},
        {"title": "用例13----校派课程卷面分整数", "score": "50", "rewardScore": "20", "examStatus": "4", "courseScoreType": "2"},
        {"title": "用例4----校派课程卷面分为空", "score": "", "rewardScore": "20", "examStatus": "4", "courseScoreType": "2"},
        {"title": "用例5----校派课程卷面分为空,奖励分为空", "score": "", "rewardScore": "", "examStatus": "4", "courseScoreType": "2"},
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


#生产环境
#拼接建立socket的head，拼接cookie
def return_Cookie(headers):
    cookie_string = headers['Set-Cookie']
    acw_tc_match = re.search(r'acw_tc=([^;]+)', cookie_string)
    # session_match = re.search(r'SESSION=([^;]+)', cookie_string)
    server_id_match = re.search(r'SERVERID=([^;]+)', cookie_string)
    acw_tc_value = acw_tc_match.group(1)
    # session_value = session_match.group(1)
    server_id_value = server_id_match.group(1)
    Cookie = 'acw_tc=' + acw_tc_value + '; ' + 'SERVERID=' + server_id_value
    return Cookie

