from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.getStsToken import getStsToken
from api.app.usRunningExt import usNewRunningExt
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.userHome import get_info
from api.app.stdLearnInfo import stdLearnInfo



class test_10run_no_taskid(HttpRunner):
    config = (
                Config("跑步打卡传值不传taskid,同时多次打卡")
                    .verify(False)
                    .variables(**{
                    "localFile": "${read_data_number(SelClockTaskTopic_run,localFile)}",
                    "bucketName": "yzimstemp",
                    "markTaskType": "3",
                    "cycleType": "1",
                    "subType":"2",                                    #读书社:scType.2,  跑团：scType.3，  自考圈：scType.4	，同学圈：scType.1   ，职场圈：scType.5
                    "mappingIdType": "3",                             #任务打卡类型：2：读书  3：跑步    4：其他
                    "scType":"3",                                      #跑团
                    "ifRunRecord":"1",                                # 是否生成跑步记录  1：是（发帖+跑步记录）  0：否（单纯发跑步帖子）
                    "message": "success",
                    "scSource": "1",                                # 帖子来源，1.安卓，2.iOS 3. 公众号 4.上进学社 5.红包
                                }
                       )
            )
    teststeps = [
        Step(RunTestCase("获取信息").call(get_info).export(*["userId"])),
        Step(RunTestCase('获取用户报读信息').call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("获取上传图片信息").call(getStsToken).teardown_hook('${upload($accessKeyId,$accessKeySecret,$endpoint,$localFile,$bucketName)}', "scPicUrl").export(*["scPicUrl"])),
        Step(RunTestCase("习惯默认带出习惯话题").setup_hook('${update_task(905,906)}').call(SelClockTaskTopic).export(*["taskEnrollId","markContent","topicName","taskId"])),
        Step(RunTestCase("发贴跑步习惯打卡帖子").with_variables(**({"distance":"3","spendDesc":"8'0","runSecond":"0.40","runTime":"00:24:00"})).call(usNewRunningExt)),
    ]

if __name__ == '__main__':
    test_10run_no_taskid().test_start()