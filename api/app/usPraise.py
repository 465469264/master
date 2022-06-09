from httprunner import HttpRunner, Config, Step, RunRequest
#点赞活动
class usPraise(HttpRunner):
    config = (
        Config("点赞活动")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                        "fabulousNum": "$fabulousNum",
                                        "praiseType": "$praiseType",
                                        "praiseId": "$praiseId",
                                        },
                                        "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("点赞活动")
                .post("/proxy/us/usPraise/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "$app_auth_token",

            }
            )
                .with_data('$data')
                .validate()
                .assert_equal("body.message", "success")
        )
    ]
if __name__ == '__main__':
    usPraise().test_start()


