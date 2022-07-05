from httprunner import HttpRunner, Config, Step, RunRequest
# 学籍信息
class stdLearnInfo(HttpRunner):
    config = (
        Config("获取学员报读信息")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("获取学员报读信息")
                .post("/proxy/mkt/stdLearnInfo/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.learnInfos[0].scholarship", "scholarship")
                .with_jmespath("body.body.learnInfos[0].learnId", "learnId")
                .with_jmespath("body.body.std_name","std_name")
                .with_jmespath("body.body.learnInfos[0].unvsId", "unvsId")
                .with_jmespath("body.body.stdId","stdId")
                .with_jmespath("body.body.mobile", "mobile")
                .with_jmespath("body.body.learnInfos[0].grade", "grade")
                .with_jmespath("body.body.learnInfos[0].unvsName", "unvsName")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]

if __name__ == '__main__':
    stdLearnInfo().test_start()