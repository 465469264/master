from httprunner import HttpRunner, Config, Step, RunRequest
#获取防重复zmtoken
class get_zmtoken(HttpRunner):
    config = (
        Config("获取zmtoken")
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
            RunRequest("获取zmtoken")
                .post("/proxy/proxy/getCommitToken/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body", "zmtoken")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    get_zmtoken().test_start()