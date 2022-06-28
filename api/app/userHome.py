from httprunner import HttpRunner, Config, Step, RunRequest
#APP获取个人信息
class get_info(HttpRunner):
    config = (
        Config("登录后获取个人信息")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": '{"header": {"appType": "3"},'
                                    '"body":{"android_phoneModel":"SM-N9500","android_version":"7.18.2","android_sdk":28}}',
                          "data": "${base64_encode($number)}"
                          })
    )
    teststeps = [
        Step(
            RunRequest("获取个人信息")
                .post("/proxy/us/userHome/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                "Content-Length": "308"
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.userId", "userId")
                .with_jmespath("body.body.mobile", "mobile")
                .with_jmespath("body.body.nickname", "nickname")
                .with_jmespath("body.body.realName", "realName")
                .with_jmespath("body.body.stdName", "stdName")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]