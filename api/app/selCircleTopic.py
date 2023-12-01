from httprunner import HttpRunner, Config, Step, RunRequest
# 话题词
class SelCircleTopic(HttpRunner):
    config = (
        Config("圈子-加载话题")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                               "header": {"appType": "${ENV(appType)}"},
                               "body": {
                                        "type": "$type",                  #0/为空>返回所有     1>返回习惯打卡话题
                                        "pageSize": "$pageSize",
                                        "pageNum": "$pageNum"
                                    }
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("圈子-加载话题")
                .post("/proxy/us/selCircleTopic/1.0/")
                .with_headers(**{
                                    "User-Agent": "${ENV(User-Agent)}",
                                    "Content-Type": "text/yzedu+; charset=UTF-8",
                                    "Host": "${ENV(app_Host)}",
                                    "authtoken": "${ENV(app_auth_token)}",
                                    }
                              )
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].topicName","topicName")
                .with_jmespath("body.body[0].id", "id")
                .validate()
                .assert_equal("body.message", "$message")

        )
    ]
