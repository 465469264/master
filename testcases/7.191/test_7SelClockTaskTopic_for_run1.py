from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.loginOrRegister import app_login

class TestCasesSelClockTaskTopic_for_run(HttpRunner):
    config = (
        Config("老师身份习惯跑步打卡话术")
            .verify(False)
            .variables(**{"mobile": "${read_data_number(accountnumber,teacher_student6)}",
                          "taskId": "${read_data_number(SelClockTaskTopic_run,taskid)}"
                          })
            )
    teststeps = [
        Step(RunTestCase("登录学员和老师账号").call(app_login).teardown_hook('${update_task()}').export(*["app_auth_token","userId"])),
        Step(RunTestCase("老师+习惯：默认带出跑步绩效话题+跑步习惯话题+习惯自动话术").with_variables(**({"markTaskType":"3"})).setup_hook('${delay(60)}')
             .call(SelClockTaskTopic).teardown_hook('${judge_topic2($body)}')),
                 ]

if __name__ == '__main__':
    TestCasesSelClockTaskTopic_for_run().test_start()