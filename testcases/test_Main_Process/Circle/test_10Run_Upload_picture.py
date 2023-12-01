#跑步上传跑步记录

from httprunner import HttpRunner, Config, Step, RunTestCase
from api.app.userHome import get_info
from api.app.getStsToken import getStsToken
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.usRunningExt import usNewRunningExt_Uplod

class Test_Shangjin_Run(HttpRunner):
    config = (
        Config("跑步上传跑步记录")
            .verify(False)
            .variables(**{
                            "markTaskType": "3",  # 任务打卡类型：2：读书  3：跑步    4：其他
                            "scSource": "2",  # 帖子来源，1.安卓，2.iOS 3. 公众号 4.上进学社 5.红包
                            "cycleType": "0",  # 打卡周期类型 1: 连续 2：累计   0：无
                            "scType": "3",  # 读书社:scType.2,  跑团：scType.3，  自考圈：scType.4	，同学圈：scType.1   ，职场圈：scType.5
                            "subType": "2",  # 普通贴：subType :0     1：读书贴  2：跑步贴）
                            "mappingIdType": "3",  # 外键mappingid类型（1：读书 2：自考课次 3：跑步）
                            "ifRunRecord": "1",  # 是否生成跑步记录  1：是（发帖+跑步记录）  0：否（单纯发跑步帖子）
                            "spendDesc":"8'16",                    #平均配速
                            "distance":"2.00",                         #距离
                            "fastSpendDesc": "6'35",
                            "runTime":"00:20:00",                     #跑步时长
                            "runSecond":"0.41",
                            "localFile": "${find_file(跑步上传.jpg)}",        #轨迹图路径
                            "bucketName": "${read_data_number(SelClockTaskTopic_run,bucketName)}",
                            "scText":"加油加油",
                            "historyRun":"0",      #传1历史上传            0-否
                            "message":"success",
                            "runRecordId": "",
                            "msg": "请求成功",
                            "nowtime":"${nowtime()}"
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("APP获取个人信息").call(get_info).export(*["nickname", "realName", "userCircleRole", "stdName","userId"])),
        Step(RunTestCase("获取上传图片信息").call(getStsToken).teardown_hook('${upload($accessKeyId,$accessKeySecret,$endpoint,$localFile,$bucketName)}', "scPicUrl").export(*["scPicUrl"])),
        Step(RunTestCase("习惯默认带出习惯话题").call(SelClockTaskTopic).export(*["taskEnrollId", "markContent", "topicName", "taskId"])),
        Step(RunTestCase("发贴跑步-上传图片").call(usNewRunningExt_Uplod)),

    ]

if __name__ == "__main__":
    Test_Shangjin_Run().test_start()