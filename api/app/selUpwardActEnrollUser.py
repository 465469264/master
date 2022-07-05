#活动报名用户头像
from httprunner import HttpRunner, Config, Step, RunRequest
class selUpwardActEnrollUser(HttpRunner):
    config = (
        Config("活动报名用户头像")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                        "pageSize": "100",
                                        "pageNum": "1",
                                        "actId": "$actId"
                                        },
                                        "header":{"appType":"4"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("活动报名用户头像")
                .post("/proxy/mkt/selUpwardActEnrollUser/1.0/")
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

        )
    ]
if __name__ == '__main__':
    selUpwardActEnrollUser().test_start()


