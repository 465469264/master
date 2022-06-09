from httprunner import HttpRunner, Config, Step, RunRequest
#登录账号接口
class app_login(HttpRunner):
    config = (
        Config("APP手机号")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                    "mobile": "$mobile",
                                    "valicode": "888888",
                                    "regChannel": "6"
                                    },
                                    "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("APP手机号登录")
                .post("/proxy/us/loginOrRegister/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}"
                }
            )
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.app_auth_token", "app_auth_token")
                .with_jmespath("body.body.userInfo.userId", "userId")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]





if __name__ == '__main__':
    app_login().test_start()
