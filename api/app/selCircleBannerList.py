from httprunner import HttpRunner, Config, Step, RunRequest
# 圈子-动态页加载branner
class selCircleBannerList(HttpRunner):
    config = (
        Config("圈子-动态页加载branner")
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
            RunRequest("圈子-动态页加载branner")
                .post("/proxy/us/selCircleBannerList/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].bannerDesc","$bannerDesc")
                .validate()
                .assert_equal("body.message", "success")

        )
    ]

if __name__ == '__main__':
    selCircleBannerList().test_start()