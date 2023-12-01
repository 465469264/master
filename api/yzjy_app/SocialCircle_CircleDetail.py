from httprunner import HttpRunner, Config, Step, RunRequest
# 圈子列表-进入帖子详情
class SocialCircle_CircleDetail(HttpRunner):
    config = (
        Config("圈子列表-进入帖子详情")
            .base_url("${ENV(yzjy-app)}")
            .verify(False)
            .variables(**{
                        "number": {
                            "data": {
                                "id": "$id",                          #帖子id
                            },
                            "client": {
                                "platform": "${ENV(platform)}",
                                "appVersion": "${ENV(appVersion)}",
                                "systemVersion": "${ENV(systemVersion)}"
                            }
                                    }
                            }
                       )
                            )
    teststeps = [
        Step(
            RunRequest("圈子列表-进入帖子详情")
                .post("/proxy/bbs-server/socialCircle/circleDetail")
                .with_headers(**{
                "User-Agent": "${ENV(User-Agent)}",
                "appType": "${ENV(appType)}",
                "Content-Type": "application/json",
                "Accept-Encoding":"gzip, deflate, br",
                "Host": "${ENV(yzjy-app-Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                                }
                              )
                .with_json("$number")
                .extract()
                .with_jmespath("body.data.personalInteractiveVO.fabulous", "fabulous")     #获取到进入该帖子详情的用户是否已点赞
                .with_jmespath("body.data.userId", "userId")         #获取到帖子详情的作者userId
                .validate()
                .assert_equal("body.state.msg", "$msg")

        )
    ]

# 圈子branna-进入帖子详情
class SocialCircle_CircleDetail_banner(HttpRunner):
    config = (
        Config("圈子-进入banner的帖子详情")
            .base_url("${ENV(yzjy-app)}")
            .verify(False)
            .variables(**{
                        "number": {
                            "data": {
                                "id": "$id",                          #帖子id
                                "bannerId": "$bannerId"               #轮播图id
                            },
                            "client": {
                                "platform": "${ENV(platform)}",
                                "appVersion": "${ENV(appVersion)}",
                                "systemVersion": "${ENV(systemVersion)}"
                            }
                                    }
                            }
                       )
                            )
    teststeps = [
        Step(
            RunRequest("圈子-进入帖子详情")
                .post("/proxy/bbs-server/socialCircle/circleDetail")
                .with_headers(**{
                "User-Agent": "${ENV(User-Agent)}",
                "appType": "${ENV(appType)}",
                "Content-Type": "application/json",
                "Accept-Encoding":"gzip, deflate, br",
                "Host": "${ENV(yzjy-app-Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                                }
                              )
                .with_json("$number")
                .extract()
                .with_jmespath("body.data.personalInteractiveVO.fabulous", "fabulous")     #获取到进入该帖子详情的用户是否已点赞
                .with_jmespath("body.data.userId", "userId")         #获取到帖子详情的作者userId
                .validate()
                .assert_equal("body.state.msg", "$msg")

        )
    ]

