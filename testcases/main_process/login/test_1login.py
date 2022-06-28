#登录
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.loginOrRegister import app_login
class TestCaseCircle_Dynamics_post(HttpRunner):
    config = (
        Config("登录app")
            .verify(False)
            .variables(**{
             "mobile": "${read_data_number(ApplyRecord,mobile)}",
            "content": "测试测试",
        })
    )
    teststeps = [
        Step(RunTestCase("登录").call(app_login).teardown_hook('${w_env_token($app_auth_token)}'))
    ]

if __name__ == "__main__":
    TestCaseCircle_Dynamics_post().test_start()



