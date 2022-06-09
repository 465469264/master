from httprunner import HttpRunner, Config, Step, RunRequest

#报名活动
class enrollUpwardAct(HttpRunner):
    config = (
        Config("报名活动")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                        "actId": "$actId",
                                        "android_version": "7.19.6",
                                        "android_phoneModel": "SM-N9500",
                                        "android_sdk": 28
                                    },
                                        "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("报名活动")
                .post("/proxy/mkt/enrollUpwardAct/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "text/yzedu+; charset=UTF-8",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "$app_auth_token",

            }
            )
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "success")
        )
    ]
if __name__ == '__main__':
    enrollUpwardAct().test_start()


