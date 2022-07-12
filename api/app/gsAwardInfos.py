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


#上进分-成长新人礼---用于方便提取和判断
from httprunner import HttpRunner, Config, Step, RunRequest
class gsAwardInfos2(HttpRunner):
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
                .with_jmespath("body.body[0].rewardType", "ruleGroup0")
                .with_jmespath("body.body[0].ruleCode", "ruleCode0")
                .with_jmespath("body.body[0].id", "id0")

                .with_jmespath("body.body[1].rewardType", "rewardType")        # rewardType:   1>每日奖励  2>学习奖励  3>成长奖励
                .with_jmespath("body.body[1].ruleGroup", "ruleGroup")          # 规则组
                .with_jmespath("body.body[1].ruleCode", "ruleCode1")            #ruleCode：赠送分规则，第二个是在线累计长达30分钟
                .with_jmespath("body.body[1].id","id1")                        # 规则id
                .with_jmespath("body.body[2].ruleCode", "ruleCode2")
                .with_jmespath("body.body[2].id", "id2")
                .with_jmespath("body.body[3].ruleCode", "ruleCode3")
                .with_jmespath("body.body[3].id", "id3")
                .with_jmespath("body.body[4].ruleCode", "ruleCode4")
                .with_jmespath("body.body[4].id", "id4")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]

if __name__ == '__main__':
    gsAwardInfos().test_start()