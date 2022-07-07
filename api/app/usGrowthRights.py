#上进分-成长权益
from httprunner import HttpRunner, Config, Step, RunRequest
class usGrowthRights(HttpRunner):
    config = (
        Config("上进分-成长权益")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                        "advLevel": "$advLevel",                 #上进分等级
                                        },
                                    "header":{"appType":"4"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("上进分-成长权益")
                .post("/proxy/mkt/usGrowthRights/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")
                .assert_equal("body.body[0].name", "$name")

        )
    ]

if __name__ == '__main__':
    usGrowthRights().test_start()