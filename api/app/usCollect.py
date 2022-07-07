#收藏帖子
from httprunner import HttpRunner, Config, Step, RunRequest
class usCollect(HttpRunner):
    config = (
        Config("收藏帖子")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "isCollects": "$isCollects",                   #1>收藏   0>取消收藏
                                            "circleId": "$circleId",                        #圈子id
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
                .post("/proxy/us/usCollect/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",

                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body","body")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]

#取消收藏时，要传收藏id
class usCollect2(HttpRunner):
    config = (
        Config("收藏帖子")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "isCollects": "$isCollects",                   #1>收藏   0>取消收藏
                                            "circleId": "$circleId",                        #圈子id
                                            "id":"$id"                                      #圈子收藏id，收藏时返回，取消收藏时必传
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
                .post("/proxy/us/usCollect/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",

                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body","body")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]