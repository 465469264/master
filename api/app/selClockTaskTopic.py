from httprunner import HttpRunner, Config, Step, RunRequest
#习惯话题词
class SelClockTaskTopic(HttpRunner):
    config = (
        Config("习惯话题")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                        "body":{
                                                "markTaskType": "$markTaskType",          #任务打卡类型：2：读书  3：跑步    4：其他
                                        },
                                        "header": {"appType": "${ENV(appType)}"}
                                        },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("习惯话题")
                .post("/proxy/mkt/selClockTaskTopic/1.0/")
                .with_headers(**{
                                "User-Agent": "${ENV(User-Agent)}",
                                "Content-Type": "text/yzedu+; charset=UTF-8",
                                "Host": "${ENV(app_Host)}",
                                "authtoken": "${ENV(app_auth_token)}",
                            }
                              )
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.topicName","topicName")
                .with_jmespath("body.body.markContent", "markContent")
                .with_jmespath("body.body.taskEnrollId", "taskEnrollId")
                .with_jmespath("body.body.taskId", "taskId")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    SelClockTaskTopic().test_start()