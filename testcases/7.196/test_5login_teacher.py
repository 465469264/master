from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.loginOrRegister import app_login


from api.app.getLivesScheduleTeacherInfo import getLivesScheduleTeacherInfo
class Test_teacher_login(HttpRunner):
    config = (
        Config("登录管理员账号")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "mobile": "13729041111",         #管理员的登录账号

                        }
                       )
                )
    teststeps = [
        Step(RunTestCase("登录讲师账号").call(app_login).teardown_hook('${w_env_token($app_auth_token)}')),
    ]

if __name__ == '__main__':
    Test_teacher_login().test_start()