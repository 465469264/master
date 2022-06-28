from httprunner import HttpRunner, Config, Step, RunRequest
#活动分享
class upwardActShare(HttpRunner):
    config = (
        Config("活动分享")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                    "actId": "$actId"
                                    },
                                    "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("活动分享")
                .post("/proxy/mkt/upwardActShare/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "authtoken": "${ENV(app_auth_token)}",
                            "Host": "${ENV(app_Host)}"
                }
            )
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.body.actName", "$actName")

        )
    ]





if __name__ == '__main__':
    upwardActShare().test_start()
