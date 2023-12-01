from httprunner import HttpRunner, Config, Step, RunRequest
#APP获取个人信息
class get_info(HttpRunner):
    config = (
        Config("获取个人信息")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                            "timeStamp": "${timestap()}",
                                    },
                                        "header":{"appType":"${ENV(appType)}"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
    )
    teststeps = [
        Step(
            RunRequest("获取个人信息")
                .post("/proxy/us/userHome/1.0/")
                .with_headers(**{
                                    "User-Agent": "${ENV(User-Agent)}",
                                    "Content-Type": "text/yzedu+; charset=UTF-8",
                                    "Host": "${ENV(app_Host)}",
                                    "authtoken": "${ENV(app_auth_token)}",
                                    })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.userId", "userId")
                .with_jmespath("body.body.mobile", "mobile")
                .with_jmespath("body.body.nickname", "nickname")
                .with_jmespath("body.body.realName", "realName")
                .with_jmespath("body.body.stdName", "stdName")
                .with_jmespath("body.body.ruleType", "ruleType")
                .with_jmespath("body.body.userCircleRole", "userCircleRole")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]

if __name__ == '__main__':
    get_info().test_start()