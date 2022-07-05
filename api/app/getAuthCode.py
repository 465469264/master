from httprunner import HttpRunner, Config, Step, RunRequest

#验证旧学员身份证
class getAuthCode(HttpRunner):
    config = (
        Config("验证旧学员身份证")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                            "isUntying": "1",                   #未知字段
                                            "idCard": "$idcard",
                                            "android_version": "7.19.2",
                                            "android_sdk": 28
                                        },
                                        "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("验证旧学员身份证")
                .post("/proxy/bds/getAuthCode/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "$app_auth_token",

            }
            )
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.mobile", "oldmobile")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    getAuthCode().test_start()


