from httprunner import HttpRunner, Config, Step, RunRequest
#获取附近的发帖人
class usReadOrForward(HttpRunner):
    config = (
        Config("获取圈子数据")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "heatType": "$heatType",    #未知字段    3
                                            "type": "$type",          #未知字段   1
                                            "readNum": "$readNum",         #未知字段   1
                                            "mappingId": "$mappingId"   #圈子id
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
            RunRequest("获取附近的发帖人")
                .post("/proxy/us/usReadOrForward/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",

                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].id", "id")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    usReadOrForward().test_start()