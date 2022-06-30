from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.web.upwardActivity_sendAppMsg import upwardActivity_sendAppMsg
from api.app.enrollUpwardAct import enrollUpwardAct



class TestCasesActivity_sendAppMsg(HttpRunner):
    config = (
        Config("触发APP活动管理活动提醒")
            .verify(False)
            .variables(**{
            "actId": "${read_data_number(Activity,actId)}",
            "actName": "${read_data_number(Activity,actName)}",
        })
            )
    teststeps = [

        Step(RunTestCase("触发APP活动管理活动提醒").setup_hook("${update_activity()}").setup_hook('${login_web()}', "Cookie").call(upwardActivity_sendAppMsg)),

    ]
if __name__ == '__main__':
    TestCasesActivity_sendAppMsg().test_start()