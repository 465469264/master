from httprunner import HttpRunner, Config, Step, RunRequest
#报名活动接口
class usTaskClockEnroll(HttpRunner):
    config = (
        Config("报名活动")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                        "pfsnName": "$pfsnName",
                                        "learnId": "$learnId",
                                        "unvsName": "$unvsName",
                                        "taskId": "$taskId"
                                    },
                                    "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("报名活动")
                .post("/proxy/us/usTaskClockEnroll/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "$app_auth_token",

                }
            )
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("status_code", 200)
        )
    ]





if __name__ == '__main__':
    usTaskClockEnroll().test_start()
