from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.updateUserInfo import app_Adult_education
from api.app.userHome import get_inf0
from api.app.getCommitToken import get_zmtoken
from api.app.enroll import sign_up_education
from api.app.Register import Register

class Test_Sign_up_adult(HttpRunner):
    config = (
        Config("APP报名")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
            "mobile": "${get_not_exist_mobile()}",
            "idCard": "${idcard()}",
            "name": "${get_name()}",
            "activeName": "amylee成人教育课程活动",
            "pfsnLevelName": "1>专科升本科类",
            "recruitType": "1",
            "unvsName": "amylee成人教育学校",
            "pfsnName": "amylee成人教育",
            "taName": "广州南沙",
            "grade": "2022",
            "scholarship": "1273",
            "pfsnLevel": "1",
            "unvsId": "164690457468960222",
            "pfsnId": "164690470996983675",
            "taId": "169"
        })
            )
    teststeps = [
        Step(RunTestCase("APP手机号注册-获取注册登录的token和手机号").call(Register).teardown_hook('${write_Register_mobile(register_mobile_chengjiao,$mobile)}').export(*["app_auth_token","mobile","userId"])),
        Step(RunTestCase("获取报名zmtoken").call(get_zmtoken).export(*["zmtoken"])),
        Step(RunTestCase("报名成教").call(sign_up_education)),
    ]
if __name__ == '__main__':
    Test_Sign_up_adult().test_start()