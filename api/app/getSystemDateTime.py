from httprunner import HttpRunner, Config, Step, RunRequest
#获取系统时间
class getSystemDateTime(HttpRunner):
    config = (
        Config("获取系统时间")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": { "header": {
                                        "appType": "4",
                                    },
                                    "body": {
                                    }
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("获取系统时间")
                .post("/proxy/bds/getSystemDateTime/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                # .with_jmespath("body.body[0].bannerDesc","$bannerDesc")
                .validate()
                .assert_equal("body.message", "$message")

        )
    ]

if __name__ == '__main__':
    getSystemDateTime().test_start()