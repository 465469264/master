from httprunner import HttpRunner, Config, Step, RunRequest
# APP活动页-今日习惯打卡
class selTodayClockTaskList(HttpRunner):
    config = (
        Config("APP活动页-今日习惯打卡")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                    },
                                    "header":{"appType":"4"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("APP活动页-今日习惯打卡")
                .post("/proxy/mkt/selTodayClockTaskList/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.list[0].name","name")
                .validate()
                .assert_equal("body.message", "$message")
                .assert_equal("body.body.list[0].name", "$name")

        )
    ]

if __name__ == '__main__':
    selTodayClockTaskList().test_start()