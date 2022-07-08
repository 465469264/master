#成长权益-勋章
from httprunner import HttpRunner, Config, Step, RunRequest
class gsMedalInfos(HttpRunner):
    config = (
        Config("成长权益-勋章")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                        },
                                    "header":{"appType":"4"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("成长权益-勋章")
                .post("/proxy/mkt/gsMedalInfos/1.0/")
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
