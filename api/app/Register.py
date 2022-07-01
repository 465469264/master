from httprunner import HttpRunner, Config, Step, RunRequest
class Register(HttpRunner):
    config = (
        Config("APP手机号注册-获取注册登录的token和手机号")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{"mobile": "$mobile","android_version":"7.19.2","notPrompt":1,"android_sdk":28,"uuId":"2a74253c-7c4d-3c84-abb6-e9e72fabb9a1","valicode":"888888","regChannel":"5"},
                                    "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("注册")
                .post("/proxy/us/loginOrRegister/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
            }
            )
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.app_auth_token", "app_auth_token")
                .with_jmespath("body.body.userInfo.mobile", "mobile")
                .with_jmespath("body.body.userInfo.userId", "userId")
                .with_jmespath("body.body.userInfo.realName", "realName")

                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    Register().test_start()


