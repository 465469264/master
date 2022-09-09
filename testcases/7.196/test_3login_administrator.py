from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.loginOrRegister import app_login


from api.app.getLivesScheduleTeacherInfo import getLivesScheduleTeacherInfo
class Test_audience_login(HttpRunner):
    config = (
        Config("登录管理员")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "mobile": "13729041112",         #管理员的登录账号

                        }
                       )
                )
    teststeps = [
        Step(RunTestCase("登录管理员账号").call(app_login).teardown_hook('${w_env_token($app_auth_token)}')),
    ]

if __name__ == '__main__':
    Test_audience_login().test_start()