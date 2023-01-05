#圈子页-跑步打卡记录
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.userHome import get_info
from api.app.stdLearnInfo import stdLearnInfo
from api.app.usRunRecord import usRunRecord
from api.app.usRunningExt import usNewRunningExt
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.getStsToken import getStsToken
from api.app.delRunExt import delRunExt



class TestCaseCircle_Delete_my_run(HttpRunner):
    config = (
        Config("圈子页-跑步打卡记录")
            .verify(False)
            .variables(**{
                "pageSize": 20,
                "pageNum": 1,
                "localFile": "${read_data_number(SelClockTaskTopic_run,localFile)}",
                "bucketName": "yzimstemp",
                "markTaskType": "3",
                "topicName": "#amylee跑步测试勿删#",  # 校验的话题词
                "cycleType": "1",
                "subType": "2",  # 跑步贴
                "mappingIdType": "3",  # 跑步类型
                "scType": "3",  # 跑团
                "ifRunRecord": "0",  # 生成跑步记录
                "scSource": "1",  # 帖子来源，1.安卓，2.iOS 3. 公众号 4.上进学社 5.红包
                "message": "success"
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取用户信息，获取userId").call(get_info).export(*["userId"])),
        Step(RunTestCase('获取用户报读信息').call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("获取上传图片信息").call(getStsToken).teardown_hook('${upload($accessKeyId,$accessKeySecret,$endpoint,$localFile,$bucketName)}', "scPicUrl").export(*["scPicUrl"])),
        Step(RunTestCase("习惯默认带出习惯话题").setup_hook('${update_task(905,906)}').call(SelClockTaskTopic).export(*["taskEnrollId", "markContent", "topicName", "taskId"])),
        Step(RunTestCase("发贴跑步习惯打卡帖子").with_variables(**({"distance": "3", "spendDesc": "8'0", "runSecond": "0.40", "runTime": "00:24:00"})).call(usNewRunningExt)),
        Step(RunTestCase("圈子页的跑步记录").call(usRunRecord).export(*["mappingId","id"])),
        Step(RunTestCase("删除圈子页的跑步记录").call(delRunExt)),

    ]

if __name__ == "__main__":
    TestCaseCircle_Delete_my_run().test_start()

