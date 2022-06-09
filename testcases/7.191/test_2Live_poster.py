from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.usLivesScheduleInfos import TestZhibo
from api.app.loginOrRegister import app_login
import time
class TestCasesLIive_poster(HttpRunner):
    config = (
        Config("app直播广场获取海报")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(accountnumber,teacher_student6)}"
        })
            )
    teststeps = [
        Step(RunTestCase("登录学员和老师账号").setup_hook('${Modify_lives_schedule()}','${delay(1)}').call(app_login).export("app_auth_token","userId")),
        Step(RunTestCase("app直播广场获取海报").setup_hook('${delay(1)}').call(TestZhibo)),
                 ]

if __name__ == '__main__':
    TestCasesLIive_poster().test_start()