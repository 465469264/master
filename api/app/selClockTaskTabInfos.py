#获取习惯打卡列表下的参与人头像
from httprunner import HttpRunner, Config, Step, RunRequest
class selClockTaskTabInfos(HttpRunner):
    config = (
        Config("获取习惯打卡列表下的参与人头像")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                            "type": "$type"            # 2>读书打卡   3>跑步打卡  4>其他打卡
                                            },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("获取习惯打卡列表下的参与人头像")
                .post("/proxy/mkt/selClockTaskTabInfos/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")
                .assert_equal("body.body.name", "$name")

        )
    ]

if __name__ == '__main__':
    selClockTaskTabInfos().test_start()