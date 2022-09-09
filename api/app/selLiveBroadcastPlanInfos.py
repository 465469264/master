#讲师的---“我的直播计划”
from httprunner import HttpRunner, Config, Step, RunRequest
class selLiveBroadcastPlanInfos(HttpRunner):
    config = (
        Config("讲师---“我的直播计划")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "iOS_version": "7.19.6",
                                            "pageSize": 10,
                                            "pageNum": 1
                                            },
                                    "header":{
                                            "appType":"3"
                                            }
                                    },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("讲师---“我的直播计划")
                .post("/proxy/us/selLiveBroadcastPlanInfos/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].channelNum","channelNum")
                .with_jmespath("body.body[0].id","id")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
