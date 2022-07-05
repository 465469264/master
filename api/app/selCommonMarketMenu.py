from httprunner import HttpRunner, Config, Step, RunRequest
# 发现页的菜单
class selCommonMarketMenu(HttpRunner):
    config = (
        Config("发现页的菜单")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": { "header": {
                                        "appType": "4",
                                    },
                                    "body": {
                                        "level": "$level",        #2>2级菜单   3>3级菜单
                                        "menuType": "$menuType",     # 1>首页   2>学堂页   3>发现页   4>我的页面
                                    }
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("发现页的菜单")
                .post("/proxy/mkt/selCommonMarketMenu/1.0/")
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
    selCommonMarketMenu().test_start()