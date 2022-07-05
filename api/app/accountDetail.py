from httprunner import HttpRunner, Config, Step, RunRequest
#统计智米
class AccountDetail(HttpRunner):
    config = (
        Config("统计智米")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                            "accType": "$accType",           #accType.1	>现金账户	 2>智米	 3>滞留账户
                                        },
                                        "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("统计智米")
                .post("/proxy/ats/accountDetail/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "${ENV(app_auth_token)}",
            }
            )
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.accAmount", "accAmount")
                .validate()
                .assert_equal("body.message", "$message")
                .assert_equal("body.body.accAmount", "$accAmount")

        )
    ]
if __name__ == '__main__':
   AccountDetail().test_start()


