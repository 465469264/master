#跳转他人的主页
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

class personalHomepageStatistics(HttpRunner):
    config = (
        Config("跳转他人的主页")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{

                                        "userId": "$userId",                       #关注列表的userid

                                    },
                                    "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("跳转他人的主页")
                .post("/proxy/us/personalHomepageStatistics/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "${ENV(app_auth_token)}",
                }
            )
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")
                .assert_equal("body.body.learnInfo.realName", "$targetRealName")

        )
    ]

if __name__ == "__main__":
    personalHomepageStatistics().test_start()



