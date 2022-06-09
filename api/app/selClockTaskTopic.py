from httprunner import HttpRunner, Config, Step, RunRequest
#习惯打卡
class SelClockTaskTopic(HttpRunner):
    config = (
        Config("习惯打卡")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "markTaskType": "$markTaskType",
                                            "taskId": "$taskId"
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
            RunRequest("习惯打卡")
                .post("/proxy/mkt/selClockTaskTopic/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                "Content-Type": "base64.b64encode",
                "Host": "${ENV(app_Host)}",
                "authtoken": "$app_auth_token",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body", "body")
                .with_jmespath("body.body.taskEnrollId","taskEnrollId")
                .with_jmespath("body.body.topicName","scText")
                .with_jmespath("body.body.markContent","markContent")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    SelClockTaskTopic().test_start()