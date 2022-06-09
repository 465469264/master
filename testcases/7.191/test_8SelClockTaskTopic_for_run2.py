from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.loginOrRegister import app_login

class TestCasesSelClockTaskTopic_for_run(HttpRunner):
    config = (
        Config("老师身份没有习惯跑步打卡话术")
            .verify(False)
            .variables(**{"mobile": "${read_data_number(accountnumber,teacher2_withoutTask)}",
                       "taskId": "${read_data_number(SelClockTaskTopic_run,taskid)}"
    }
                       )

            )
    teststeps = [
        Step(RunTestCase("登录老师账号").call(app_login).export(*["app_auth_token", "userId"])),
        Step(RunTestCase("老师:默认带出跑步绩效话题+X月累计打卡X天（X月是指本月，X天是累计X天发帖，1天内不管发多少次算1天")
             .with_variables(**({"markTaskType": "3"})).call(SelClockTaskTopic).teardown_hook('${judge_topic1($body)}')),
                 ]

if __name__ == '__main__':
    TestCasesSelClockTaskTopic_for_run().test_start()