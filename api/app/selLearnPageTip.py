#不知道什么接口
from httprunner import HttpRunner, Config, Step, RunRequest
class selLearnPageTip(HttpRunner):
    config = (
        Config("学堂页的不知道什么接口")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                       "header": {
                                                    "appType": "4",
                                                },
                                        "body": {
                                                "learnId": "$learnId",
                                                    }
                                        },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("学堂页的不知道什么接口")
                .post("/proxy/us/selLearnPageTip/1.0/")
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

        )
    ]
