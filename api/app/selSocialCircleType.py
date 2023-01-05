#登陆前，获取圈子的默认列表，不需要token
from httprunner import HttpRunner, Config, Step, RunRequest
class selSocialCircleType(HttpRunner):
    config = (
        Config("登陆前，获取圈子的默认列表")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                        },
                                    "header":{
                                            "appType": "3",
                                        }
                                },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("登陆前，获取圈子的默认列表")
                .post("/proxy/us/selSocialCircleType/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.message", "$message")

        )
    ]
