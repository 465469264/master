from httprunner import HttpRunner, Config, Step, RunRequest
# 埋点
class operationStatistic(HttpRunner):
    config = (
        Config("埋点接口")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                        "targetType": "$targetType",               #target_type:事件类型
                                        "userName": "$userName",                          #分享人
                                        "platform": "$platform",                         #平台:WECHAT,IOS,Android
                                        "targetId ": "$targetId",                            #业务ID
                                        "targetReamrk": "$targetReamrk"                     #业务描述
                                },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("埋点接口")
                .post("/proxy/us/operationStatistic/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "success")
        )
    ]

if __name__ == '__main__':
    operationStatistic().test_start()