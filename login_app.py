#登录
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.proxy_us_loginOrRegister import app_login
from api.web.editPhonecode import eddit_Phone_Message


class Test_login(HttpRunner):
    config = (
        Config("登录app")
            .verify(False)
            .variables(**{
                         "mobile": "${read_data_number(ApplyRecord,mobile)}",
                        "valicode":"${read_data_number(ApplyRecord,message_cod)}"

        })
    )
    teststeps = [

        Step(RunTestCase("设置测试手机号码验证码").call(eddit_Phone_Message)),
        Step(RunTestCase("登录测试手机号").call(app_login).teardown_hook('${w_env_token($app_auth_token)}')),

    ]

if __name__ == "__main__":
    Test_login().test_start()



