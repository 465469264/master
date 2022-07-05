from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.stdLearnInfo import stdLearnInfo
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.getStsToken import getStsToken
from api.app.usRunningExt import usRunningExt
from api.app.selCircleDynamicInfos import selCircleDynamicInfos
from api.app.userHome import get_info

class Test_Run_habbit(HttpRunner):

    config = (
        Config("报跑步打卡的话术-及发帖")
            .verify(False)
            .variables(**{
            "taskId": "${read_data_number(SelClockTaskTopic_run,taskid)}",
            "localFile": "${read_data_number(SelClockTaskTopic_run,localFile)}",
            "bucketName": "yzimstemp",
            "markTaskType": "3",
            "topicName":"#amylee跑步测试勿删#",               #校验的话题词
            "cycleType": "1",
            "subType":"2",         #跑步贴
            "mappingIdType": "3",  #跑步类型
            "scType":"3",          #跑团
            "ifRunRecord":"1",        #生成跑步记录
            "own":"0",
            "message": "success"
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取信息").call(get_info).export(*["userId"])),
        Step(RunTestCase('获取用户报读信息').call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("习惯默认带出习惯话题").call(SelClockTaskTopic).export(*["taskEnrollId","markContent"])),
        Step(RunTestCase("获取上传图片信息").call(getStsToken).teardown_hook('${upload($accessKeyId,$accessKeySecret,$endpoint,$localFile,$bucketName)}', "scPicUrl").export(*["scPicUrl"])),
        Step(RunTestCase("发贴跑步习惯打卡帖子").with_variables(**({"distance":"3","spendDesc":"9'19","runSecond":"0.47","historyRun":"0","runTime":"00:27:59"})).call(usRunningExt)),
        Step(RunTestCase("查看自己的圈子").with_variables(**({"pageSize": "20", "userRoleType": 2, "pageNum": 1,"scType": "",})).call(selCircleDynamicInfos)),

    ]
if __name__ == '__main__':
    Test_Run_habbit().test_start()