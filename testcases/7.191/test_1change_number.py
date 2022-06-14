from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.getAuthCode import getAuthCode
from api.app.Register import Register
from api.app.untyingMobile import untyingMobile
class TestCaseschange_number(HttpRunner):
    config = (
        Config("更换手机号码")
            .verify(False)
            .variables(**{
            "idcard": "${read_data_number(test_data,idcard)}",
            "mobile": "${get_not_exist_mobile()}",
        })
            )
    teststeps = [
        Step(RunTestCase("APP手机号注册-获取注册登录的token和手机号").call(Register).teardown_hook
             ('${w_env($mobile)},${write_Register_mobile($mobile)}').export(*["app_auth_token","mobile","userId"])),
        Step(RunTestCase("验证需要解绑的学员身份证").setup_hook('${delay(1)}').call(getAuthCode).export(*["oldmobile"])),
        Step(RunTestCase("验证需要解绑的学员身份证").call(untyingMobile)),
                 ]

if __name__ == '__main__':
    TestCaseschange_number().test_start()