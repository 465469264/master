from httprunner import HttpRunner, Config, Step, RunRequest
#APP改名字
class app_Adult_education(HttpRunner):
    config = (
        Config("改名")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{"mobile": "${get_not_exist_mobile()}",
                          "name":"${get_name()}",
                          "number": '{"header": {"appType": "3"},'
                                    '"body":{"realName":"$name","android_phoneModel":"SM-N9500","nickname":"zmc_zftmqusy","android_version":"7.18.2","android_sdk":28}}',
                          "data": "${base64_encode($number)}"
                          })
            )
    teststeps = [
        Step(
            RunRequest("注册后修改名字")
                .post("/proxy/us/updateUserInfo/1.0/")
                .with_headers(**{
                                "User-Agent":"Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                                "Content-Type":"text/yzedu+; charset=UTF-8",
                                 "Host": "${ENV(app_Host)}",
                                "authtoken":"${ENV(register_app_auth_token)}",
                                "deviceId":"2a74253c-7c4d-3c84-abb6-e9e72fabb9a1",
                                "Content-Length":"308"
                                })
                .with_data('$data')
                .validate()
                .assert_equal("status_code", 200)
        )
    ]