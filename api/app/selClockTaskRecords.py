from httprunner import HttpRunner, Config, Step, RunRequest
# 查看习惯 打卡进度
class selClockTaskRecords(HttpRunner):
    config = (
        Config("查看习惯 打卡进度")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                        "taskId": "$taskId",                                     #活动/习惯详情
                                        "userId": "$userId",
                                    },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("查看习惯 打卡进度")
                .post("/proxy/mkt/selClockTaskRecords/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")

        )
    ]

if __name__ == '__main__':
    selClockTaskRecords().test_start()