from httprunner import HttpRunner, Config, Step, RunRequest
# APP查看成绩
class selStdAchievement(HttpRunner):
    config = (
        Config("APP查看成绩")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                            "semester": "$semester",
                                            "learnId": "$learnId",

                                    },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("APP查看成绩")
                .post("/proxy/bds/selStdAchievement/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "$app_auth_token",
            })
                .with_data('$data')
                .extract()
                # .with_jmespath("body.body.achievementInfo[0].usualTimeMark","usualTimeMark")
                .validate()
                .assert_equal("body.body.achievementInfo[0].usualTimeMark", "$usualTimeMark")
                .assert_equal("body.body.achievementInfo[0].score", "$score")
                .assert_equal("body.body.achievementInfo[0].rewardScore", "$rewardScore")
                # .assert_equal("body.body.achievementInfo[0].totalScore", "$totalScore")
                .assert_equal("body.body.achievementInfo[0].isPass", "$isPass")
                .assert_equal("body.message", "success")

        )
    ]

if __name__ == '__main__':
    selStdAchievement().test_start()