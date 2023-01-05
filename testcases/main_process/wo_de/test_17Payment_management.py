from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.Register import Register
class Payment_management(HttpRunner):
    config = (
        Config("缴费管理-申请电子收据")
            .verify(False)
            .variables(**{
                            "mobile": "13958685688",               #报考城市为惠州
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("登录").call(Register).export(*["app_auth_token"])),
    ]
if __name__ == '__main__':
    Payment_management().test_start()