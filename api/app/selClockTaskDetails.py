from httprunner import HttpRunner, Config, Step, RunRequest
# 查看习惯详情
class selClockTaskDetails(HttpRunner):
    config = (
        Config("查看习惯详情")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                        "taskId": "$taskId",                                     #活动/习惯详情
                                        "userId": "$userId",
                                    },
                                    "header": {"appType": "${ENV(appType)}"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("查看习惯详情")
                .post("/proxy/mkt/selClockTaskDetails/1.0/")
                .with_headers(**{
                                    "User-Agent": "${ENV(User-Agent)}",
                                    "Content-Type": "text/yzedu+; charset=UTF-8",
                                    "Host": "${ENV(app_Host)}",
                                    "authtoken": "${ENV(app_auth_token)}",
                                    }
                              )
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")

        )
    ]

if __name__ == '__main__':
    selClockTaskDetails().test_start()