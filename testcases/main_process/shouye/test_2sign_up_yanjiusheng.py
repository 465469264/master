from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.getCommitToken import get_zmtoken
from api.app.enroll import sign_up_education
from api.app.Register import Register

class Test_Sign_up_yanjiusheng(HttpRunner):
    config = (
        Config("APP报名研究生")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
            "mobile": "${get_not_exist_mobile()}",
            "idCard": "${idcard()}",
            "name": "${get_name()}",
            "activeName": "amylee研究生必过面试",
            "pfsnLevelName": "6>硕士研究生",
            "recruitType": "1",
            "unvsName": "amylee研究生学校",
            "pfsnName": "amylee培训",
            "taName": "广州市辖",
            "grade": "2022",
            "scholarship": "1272",
            "pfsnLevel": "6",
            "unvsId": "164673093611618401",
            "pfsnId": "164673098206016400",
            "taId": "155184016465430588"
        })
            )
    teststeps = [
        Step(RunTestCase("APP手机号注册-获取注册登录的token和手机号").call(Register).teardown_hook('${write_Register_mobile(register_mobile_yanjiusheng,$mobile)}').export(*["app_auth_token","mobile","userId"])),
        Step(RunTestCase("获取报名zmtoken").call(get_zmtoken).export(*["zmtoken"])),
        Step(RunTestCase("报名研究生").call(sign_up_education)),
    ]
if __name__ == '__main__':
    Test_Sign_up_yanjiusheng().test_start()