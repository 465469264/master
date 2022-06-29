from httprunner import HttpRunner, Config, Step, RunRequest
# 习惯任务-我的战绩
class usTaskClockRecord(HttpRunner):
    config = (
        Config("习惯任务-我的战绩")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                    },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("习惯任务-我的战绩")
                .post("/proxy/mkt/usTaskClockRecord/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].id","id")
                .with_jmespath("body.body[0].name", "name")
                .validate()
                .assert_equal("body.message", "success")

        )
    ]

if __name__ == '__main__':
    usTaskClockRecord().test_start()