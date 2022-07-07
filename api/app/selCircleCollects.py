#我的圈子-收藏帖子列表
from httprunner import HttpRunner, Config, Step, RunRequest
class selCircleCollects(HttpRunner):
    config = (
        Config("收藏帖子")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "pageSize": "$pageSize",
                                            "userId": "$userId",
                                            "pageNum": "$pageNum"
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
            RunRequest("收藏帖子")
                .post("/proxy/us/selCircleCollects/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
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

