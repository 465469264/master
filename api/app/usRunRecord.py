#圈子页的跑步记录
from httprunner import HttpRunner, Config, Step, RunRequest
class usRunRecord(HttpRunner):
    config = (
        Config("圈子页的跑步记录")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "pageSize": "$pageSize",            #尺寸
                                            "userId": "$userId",
                                            "pageNum": "$pageNum",          #页码

                                        },
                                    "header":{
                                            "appType": "3",
                                        }
                                },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("获取跑步记录")
                .post("/proxy/us/usRunRecord/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",

                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.runList[0].id", "id")
                .with_jmespath("body.body.runList[0].mappingId", "mappingId")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]