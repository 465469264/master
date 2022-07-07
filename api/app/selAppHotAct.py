from httprunner import HttpRunner, Config, Step, RunRequest
#首页热门推荐活动接口
class selAppHotAct(HttpRunner):
    config = (
        Config("首页热门推荐活动接口")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": { "header": {
                                        "appType": "4",
                                    },
                                    "body": {
                                        "menuType": "$menuType",              #1>首页
                                    }
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("首页热门推荐活动接口")
                .post("/proxy/us/selAppHotAct/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.upwardActInfo[0].id","id")
                .validate()
                .assert_equal("body.message", "$message")

        )
    ]

if __name__ == '__main__':
    selAppHotAct().test_start()