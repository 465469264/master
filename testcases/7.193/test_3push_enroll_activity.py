from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.enrollUpwardAct import enrollUpwardAct
from api.app.Register import Register
from api.app.selAppMsgCenter import selAppMsgCenter

class TestCasesenrollUpwardAct_sendAppMsg(HttpRunner):
    config = (
        Config("报名活动触发提醒")
            .verify(False)
            .variables(**{"mobile": "${get_not_exist_mobile()}",
                          "actId": "${read_data_number(Activity,actId)}"
                          })
            )
    teststeps = [
        Step(RunTestCase("APP手机号注册-").call(Register).export(*["app_auth_token"])),
        Step(RunTestCase("报名活动触发提醒").call(enrollUpwardAct)),
        Step(RunTestCase("判断报名成功后消息提醒").setup_hook('${delay(1)}').call(selAppMsgCenter).teardown_hook(
            '${selAppMsgCenter_msgtype2($body)}')),
    ]
if __name__ == '__main__':
    TestCasesenrollUpwardAct_sendAppMsg().test_start()