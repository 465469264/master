#成长任务-达到任务送上进分
from httprunner import HttpRunner, Config, Step, RunRequest
class gsOnlineRecord(HttpRunner):
    config = (
        Config("成长任务-达到任务送上进分")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                            "time": "$time",                         #在线时间
                                            "rewardType": "$rewardType",            # rewardType:   1>每日奖励  2>学习奖励  3>成长奖励
                                            "ruleCode": "$ruleCode",                  #规则
                                            "unit": "$unit",                         #根据符合每日奖励的返回序号
                                            "ruleGroup": "$ruleGroup",                #规则组
                                            "id": "$id",                             #规则id
                                        },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("成长任务-达到任务送上进分")
                .post("/proxy/mkt/gsOnlineRecord/1.0/")
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


#成长任务-登录送上进分
from httprunner import HttpRunner, Config, Step, RunRequest
class gsOnlineRecord2(HttpRunner):
    config = (
        Config("成长任务-登录送上进分")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                            "rewardType": "$rewardType",            # rewardType:   1>每日奖励  2>学习奖励  3>成长奖励
                                            "ruleCode": "$ruleCode",                  #规则
                                            "ruleGroup": "$ruleGroup",                #规则组
                                            "id": "$id",                             #规则id
                                        },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("成长任务-登录送上进分")
                .post("/proxy/mkt/gsOnlineRecord/1.0/")
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
