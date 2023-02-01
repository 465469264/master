#获取任务中心列表的所有任务
from httprunner import HttpRunner, Config, Step, RunRequest
class myTasks(HttpRunner):
    config = (
        Config("获取任务中心列表的待完成任务")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "learnId": "$learnId",
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
            RunRequest("获取任务中心列表的待完成任务")
                .post("/proxy/mkt/myTasks/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.list[0].taskId","taskId")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]

class myTasks2(HttpRunner):
    config = (
        Config("获取任务中心列表的已失效任务/////已完成列表的任务")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "learnId": "$learnId",
                                            "pageSize": 50,
                                            "tabType": "$tabType",                                          #1>已完成   #2>已失效
                                            "isSticky": "1",
                                            "pageNum": 1,
                                            "taskStatus": "$taskStatus"                                  #传空>已失效     1>已完成
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
            RunRequest("获取任务中心列表的已失效任务/////已完成列表的任务")
                .post("/proxy/mkt/myTasks/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.list[0].taskId","taskId")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]