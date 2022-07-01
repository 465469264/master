from httprunner import HttpRunner, Config, Step, RunRequest
#生成报名付费活动订单
class createUpwardActOrder(HttpRunner):
    config = (
        Config("生成报名付费活动订单")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                        "learnId": "$learnId",
                                        "actId": "$actId"                    #活动id
                                    },
                                    "header": {"appType": "3"}
                                    },
                    "data": "${base64_encode($number)}",

        }
                       )
        )
    teststeps = [
        Step(
            RunRequest("生成报名付费活动订单")
                .post("/proxy/bds/createUpwardActOrder/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "authtoken": "${ENV(app_auth_token)}",
                            "Host": "${ENV(app_Host)}"
                }
            )
                .with_data('$data')
                .extract()
                .with_jmespath("body.body", "body")                #活动付费订单id
                .validate()
                .assert_equal("status_code", 200)
        )
    ]





if __name__ == '__main__':
    createUpwardActOrder().test_start()
