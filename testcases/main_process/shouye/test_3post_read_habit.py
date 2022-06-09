from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.loginOrRegister import app_login
from api.app.stdLearnInfo import stdLearnInfo
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.selUsNewBookDetail import selUsNewBookDetail
from api.app.usReadExt import usReadExt


class Test_Read_habbit(HttpRunner):
    config = (
        Config("读书打卡话术-打卡")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(accountnumber,teacher_student6)}",
            "taskId": "${read_data_number(SelClockTaskTopic_read,taskid)}",
            "localFile": "${read_data_number(SelClockTaskTopic_run,localFile)}",
            "bucketName": "yzimstemp",

                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("登录测试账号").call(app_login).export(*["app_auth_token","userId"])),
        Step(RunTestCase('获取用户报读信息').call(stdLearnInfo).export(*["learnId","pfsnName"])),
        Step(RunTestCase("老师+习惯：默认带出读书绩效话题+读书习惯话题+习惯自动话术").with_variables(**({"markTaskType": "2"})).call(SelClockTaskTopic).teardown_hook('${judge_topic4($body)}')
             .export(*["taskEnrollId","scText","markContent"])),
        Step(RunTestCase("带出书籍").with_variables(**({"markTaskType": "2"})).call(selUsNewBookDetail).export(*["name","imgUrl","readPersonNum","bookId"])),
        Step(RunTestCase("发贴读书习惯打卡帖子").with_variables(**({"cycleType": "1","subType":"1","scType": "2","markTaskType": "2"})).call(usReadExt))

    ]
if __name__ == '__main__':
    Test_Read_habbit().test_start()