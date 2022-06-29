from httprunner import HttpRunner, Config, Step, RunRequest
#删除帖子
class usSetDynamics(HttpRunner):
    config = (
        Config("删除帖子")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                        "status": "$status",                         #0>禁用  1>启用  3>删除）
                                        "id": "$id",                         #圈子id
                                        "circleUserId": "$circleUserId",       #发帖人的userid
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
            RunRequest("删除帖子")
                .post("/proxy/us/usSetDynamics/1.0/")
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
                .assert_equal("status_code", 200)
        )
    ]
