from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.selAppHpMarketMenu import selAppHpMarketMenu
from api.app.loginOrRegister import app_login
from api.app.selAppMsgCenter import selAppMsgCenter

class TestCaseschicken_message(HttpRunner):
    config = (
        Config("统计首页小鸡的未读消息")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(accountnumber,teacher_student6)}",
            "level":"2",
            "menuType":"1"
        })
            )
    teststeps = [
        Step(RunTestCase("登录学员和老师账号").setup_hook('${delay(1)}').call(app_login).export(*["app_auth_token","userId"])),
        Step(RunTestCase("判断消息通知@和评论的newUnReadNum").call(selAppMsgCenter)
             .export(*["newUnReadNum1","newUnReadNum2","newUnReadNum4","newUnReadNum5","newUnReadNum7","newUnReadNum8","newUnReadNum9","newUnReadNum10"])),
        Step(RunTestCase("统计首页小鸡的新消息newUnReadNum").with_variables(**{"ls":["$newUnReadNum1","$newUnReadNum2","$newUnReadNum4","$newUnReadNum5","$newUnReadNum7","$newUnReadNum8","$newUnReadNum9","$newUnReadNum10"]})
             .call(selAppHpMarketMenu).teardown_hook('${judge_newUnReadNum2($ls,$unReadMsgNum)}')),
                 ]

if __name__ == '__main__':
    TestCaseschicken_message().test_start()