from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.loginOrRegister import app_login

class TestCasesSelClockTaskTopic_for_run(HttpRunner):
    config = (
        Config("学员身份习惯跑步打卡话术")
            .verify(False)
            .variables(**{"mobile": "${read_data_number(accountnumber,student4)}",
                          "taskId": "${read_data_number(SelClockTaskTopic_run,taskid)}"
                          }
                       )
            )
    teststeps = [
        Step(RunTestCase("学员student4").call(app_login).export(*["app_auth_token", "userId"])),
        Step(RunTestCase("其他用户+习惯，默认带出习惯话题+习惯自动话术").with_variables(**({"markTaskType": "3"})).call(SelClockTaskTopic).teardown_hook('${judge_topic3($body)},${delay(1)}'))
                 ]

if __name__ == '__main__':
    TestCasesSelClockTaskTopic_for_run().test_start()