from httprunner import HttpRunner, Config, Step, RunRequest
# 学堂页的学习报告
class usStudyReport(HttpRunner):
    config = (
        Config("学堂页的学习报告")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                       "header": {
                                                    "appType": "4",
                                                },
                                        "body": {
                                                "learnId": "$learnId",
                                                    }
                                        },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("学堂页的学习报告")
                .post("/proxy/us/usStudyReport/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].businessType","businessType")           #businessType  2>读书会	3>跑团	98>考试成绩	100>习惯报名数
                .validate()
                .assert_equal("body.message", "$message")

        )
    ]
