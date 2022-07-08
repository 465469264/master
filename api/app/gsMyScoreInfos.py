#我的上进分-明细
from httprunner import HttpRunner, Config, Step, RunRequest
class gsMyScoreInfos(HttpRunner):
    config = (
        Config("我的上进分-明细")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                        "pageSize": "$pageSize",
                                        "term": "$term",
                                        "pageNum": "$pageNum"
                                        },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("我的上进分-明细")
                .post("/proxy/mkt/gsMyScoreInfos/1.0/")
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
                .assert_equal("body.body[0].behaviorDesc", "$behaviorDesc")
        )
    ]
