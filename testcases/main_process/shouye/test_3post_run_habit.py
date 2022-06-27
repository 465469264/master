from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.loginOrRegister import app_login
from api.app.usTaskClockEnroll import usTaskClockEnroll
from api.app.stdLearnInfo import stdLearnInfo
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.getStsToken import getStsToken
from api.app.usRunningExt import usRunningExt

class Test_Run_habbit(HttpRunner):
    config = (
        Config("报跑步打卡的话术-及发帖")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(accountnumber,teacher_student6)}",
            "taskId": "${read_data_number(SelClockTaskTopic_run,taskid)}",
            "localFile": "${read_data_number(SelClockTaskTopic_run,localFile)}",
            "bucketName": "yzimstemp",

                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("登录测试账号").call(app_login).export(*["app_auth_token","userId"])),
        Step(RunTestCase('获取用户报读信息').call(stdLearnInfo).export(*["learnId","pfsnName"])),
        Step(RunTestCase("老师+学生身份+习惯，默认带出习惯话题+习惯自动话术").with_variables(**({"markTaskType": "3"})).call(SelClockTaskTopic)
             .teardown_hook('${judge_topic2($body)},${delay(1)}').export(*["taskEnrollId","scText","markContent"])),
        Step(RunTestCase("获取上传图片信息").call(getStsToken).teardown_hook('${upload($accessKeyId,$accessKeySecret,$endpoint,$localFile,$bucketName)}', "scPicUrl").export(*["scPicUrl"])),
        Step(RunTestCase("发贴跑步习惯打卡帖子").with_variables(**({"cycleType":"1","runTime":"00:27:59","distance":"3","subType":"2","markTaskType":"3",
                                                          "mappingIdType":"3","scType":"3","ifRunRecord":"1"})).call(usRunningExt)),

        ]
if __name__ == '__main__':
    Test_Run_habbit().test_start()