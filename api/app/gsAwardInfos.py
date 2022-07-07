#上进分-成长新人礼
from httprunner import HttpRunner, Config, Step, RunRequest
class gsAwardInfos(HttpRunner):
    config = (
        Config("上进分-成长新人礼")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                        "learnId": "$learnId",
                                        "type": "$type",                #1>成长新人礼   2>每日奖励      3>学习奖励    4 >成长奖励
                                        },
                                    "header":{"appType":"4"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("上进分-成长新人礼")
                .post("/proxy/mkt/gsAwardInfos/1.0/")
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

        )
    ]

if __name__ == '__main__':
    gsAwardInfos().test_start()