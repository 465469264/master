from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.sign import sign
from api.app.isSign import isSign
from api.app.getSignInfo import getSignInfo

class Test_qiandao(HttpRunner):
    config = (
        Config("用户签到")
            .verify(False)
            .variables(**{
                            "message": "success",
                            }
                       )
            )
    teststeps = [
        Step(RunTestCase("获取学员是否已签到").call(isSign).teardown_hook('${judge_sing($body)}', "message1").export(*["message1"])),
        Step(RunTestCase("签到").with_variables(**({"message":"$message1"})).call(sign)),
        Step(RunTestCase("获取签到信息").call(getSignInfo)),

    ]
if __name__ == '__main__':
    Test_qiandao().test_start()