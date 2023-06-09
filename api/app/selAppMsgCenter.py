from httprunner import HttpRunner, Config, Step, RunRequest
#APP消息通知
class selAppMsgCenter(HttpRunner):
    config = (
        Config("消息通知列表")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": '{"header": {"appType": "3"},'
                                    '"body":{"android_phoneModel":"SM-N9500","android_version":"7.18.2","android_sdk":28}}',
                          "data": "${base64_encode($number)}"
                          })
    )
    teststeps = [
        Step(
            RunRequest("消息通知列表")
                .post("/proxy/us/selAppMsgCenter/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body","body")
                .with_jmespath("body.body[1].newUnReadNum", "newUnReadNum1")
                .with_jmespath("body.body[2].newUnReadNum", "newUnReadNum2")
                .with_jmespath("body.body[4].newUnReadNum", "newUnReadNum4")
                .with_jmespath("body.body[5].newUnReadNum", "newUnReadNum5")
                .with_jmespath("body.body[7].newUnReadNum", "newUnReadNum7") #@我
                .with_jmespath("body.body[8].newUnReadNum", "newUnReadNum8")
                .with_jmespath("body.body[9].newUnReadNum", "newUnReadNum9") #评论
                .with_jmespath("body.body[10].newUnReadNum", "newUnReadNum10")
                .validate()
                .assert_equal("body.body[0].title", "小y")
                .assert_equal("body.body[1].title", "学习提醒")
                .assert_equal("body.message", "$message")
        )
    ]

if __name__ == '__main__':
    selAppMsgCenter().test_start()