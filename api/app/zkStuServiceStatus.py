from httprunner import HttpRunner, Config, Step, RunRequest
#APP获取个人信息
class zkStuServiceStatus(HttpRunner):
    config = (
        Config("登录后获取个人信息")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number":{
                                    "body": {
                                        "learnId": "$learnId",
                                    },
                                    "header": {
                                        "appType": "4",
                                    }
                                },
                          "data": "${base64_encode($number)}",
                          }
                       )
    )
    teststeps = [
        Step(
            RunRequest("获取个人信息")
                .post("/proxy/us/zkStuServiceStatus/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                "Content-Length": "308"
            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]