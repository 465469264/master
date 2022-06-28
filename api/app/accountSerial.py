from httprunner import HttpRunner, Config, Step, RunRequest
#智米记录
class AccountSerial(HttpRunner):
    config = (
        Config("智米收入记录")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                            "accType": "$accType",           #2
                                            "pageSize": "$pageSize",
                                            "pageNum": "$pageNum"
                                        },
                                        "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("智米记录")
                .post("/proxy/ats/accountSerial/1.0/")
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
                .assert_equal("body.message", "success")
                .assert_equal("body.body[$a].amount", "$amount")

        )
    ]
if __name__ == '__main__':
   AccountSerial().test_start()


