from httprunner import HttpRunner, Config, Step, RunRequest
# APP首页消息
class selAppHpMarketMenu(HttpRunner):
    config = (
        Config("APP首页小鸡的未读消息")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                        "level": "$level",
                                        "menuType": "$menuType",
                                        "android_version": "7.19.6",
                                        "android_sdk": 28
                                    },
                                        "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("APP首页小鸡的未读消息")
                .post("/proxy/mkt/selAppHpMarketMenu/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.msgInfo.unReadMsgNum", "unReadMsgNum")
                .with_jmespath("body.body.marketInfo[0][0].menuName","menuName")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
