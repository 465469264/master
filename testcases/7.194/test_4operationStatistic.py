from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.operationStatistic import operationStatistic
from api.app.loginOrRegister import app_login
from api.app.selCircleDynamicInfos import selCircleDynamicInfos

class Test_perationStatistic(HttpRunner):
    config = (
        Config("埋点")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(accountnumber,teacher2)}",
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("登录测试账号").call(app_login).export(*["app_auth_token","userId","realName"])),
        Step(RunTestCase("帖子海报埋点").with_variables(**({"targetType":"poster_circle_detail","userName":"$realName","platform":"IOS","targetId":"19","targetReamrk":"帖子海报"})).call(operationStatistic)),
        Step(RunTestCase("活动海报埋点").with_variables(**({"targetType":"poster_activity", "userName": "$realName", "platform": "IOS", "targetId": "20","targetReamrk": "活动海报"})).call(operationStatistic)),
        Step(RunTestCase("习惯海报埋点").with_variables(**({"targetType": "poster_habit", "userName": "$realName", "platform": "IOS", "targetId": "21","targetReamrk": "习惯海报"})).call(operationStatistic)),

    ]

if __name__ == '__main__':
    Test_perationStatistic().test_start()