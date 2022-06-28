from httprunner import HttpRunner, Config, Step, RunRequest
# @我消息一键已读
class updateInMessageRead(HttpRunner):
    config = (
        Config("消息列表-@我一键已读")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                            "msgType": "$a"
                                        },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("消息列表-@我一键已读")
                .post("/proxy/bds/updateInMessageRead/1.0/")
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
    updateInMessageRead().test_start()