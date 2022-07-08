#成长权益-智米奖励
from httprunner import HttpRunner, Config, Step, RunRequest
class gsLevelRewardInfos(HttpRunner):
    config = (
        Config("成长权益-智米奖励")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                        },
                                    "header":{"appType":"4"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("成长权益-智米奖励")
                .post("/proxy/mkt/gsLevelRewardInfos/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.levelRewardInfos[0].id","id")           #提取第一个任务
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
