from httprunner import HttpRunner, Config, Step, RunRequest

#解绑手机号码
class untyingMobile(HttpRunner):
    config = (
        Config("解绑手机号")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                            "oldMobile": "$oldmobile",
                                            "mobile": "$mobile",
                                            "android_version": "7.19.2",
                                            "android_sdk": 28,
                                            "valicode": "888888"
                                        },
                                        "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("解绑身份证")
                .post("/proxy/us/untyingMobile/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "$app_auth_token",

            }
            )
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    untyingMobile().test_start()


