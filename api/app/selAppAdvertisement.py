from httprunner import HttpRunner, Config, Step, RunRequest
#首页广告弹窗
class selAppAdvertisement(HttpRunner):
    config = (
        Config("首页广告弹窗")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": { "header": {
                                        "appType": "3",
                                                },
                                    "body": {
                                        "adFirstType": "1"             #1广告  2启动页
                                            }
                                    },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("首页广告弹窗")
                .post("/proxy/mkt/selAppAdvertisement/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].activityName","activityName")
                .validate()
                .assert_equal("body.body[0].activityName","$activityName")
                .assert_equal("body.message", "$message")

        )
    ]

if __name__ == '__main__':
    selAppAdvertisement().test_start()