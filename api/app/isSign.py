from httprunner import HttpRunner, Config, Step, RunRequest
# 判断是否已签到
class isSign(HttpRunner):
    config = (
        Config("判断是否已签到")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                        },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("判断是否已签到")
                .post("/proxy/us/isSign/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body","body")
                .validate()
                .assert_equal("body.message", "success")

        )
    ]

if __name__ == '__main__':
    isSign().test_start()