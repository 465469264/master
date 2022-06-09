from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.loginOrRegister import app_login

class TestCasesSelClockTaskTopic_for_run(HttpRunner):
    config = (
        Config("老师+学员身份习惯读书笔记发帖话术")
            .verify(False)
            .variables(**{"mobile": "${read_data_number(accountnumber,teacher_student6)}",
                          "taskId": "${read_data_number(SelClockTaskTopic_read,taskId)}"
                          })
            )
    teststeps = [
        Step(RunTestCase("登录学员和老师账号").call(app_login).export(*["app_auth_token","userId"])),
        Step(RunTestCase("老师+习惯：默认带出读书绩效话题+读书习惯话题+习惯自动话术")
             .with_variables(**({"markTaskType": "2"})).
             call(SelClockTaskTopic).teardown_hook('${judge_topic4($body)}')),
                 ]

if __name__ == '__main__':
    TestCasesSelClockTaskTopic_for_run().test_start()