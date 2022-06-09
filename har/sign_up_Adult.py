from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.updateUserInfo import app_Adult_education
from api.app.userHome import get_inf0
from api.app.getCommitToken import get_zmtoken
from api.app.enroll import sign_up_education
from api.app.Register import Register

class TestCasesSign_up_adult(HttpRunner):
    config = (
        Config("APP报名成教")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
            "mobile": "${get_not_exist_mobile()}",
            "idCard": "${idcard()}",
            "name": "${get_name()}",

        })
            )
    teststeps = [
        Step(RunTestCase("APP手机号注册-获取注册登录的token和手机号").call(Register).teardown_hook('${write_Register_mobile($mobile)}').export(*["app_auth_token","mobile","userId"])),
        Step(RunTestCase("获取报名zmtoken").call(get_zmtoken).export(*["zmtoken"])),
        Step(RunTestCase("报名成教").call(sign_up_education)),
    ]
if __name__ == '__main__':
    TestCasesSign_up_adult().test_start()