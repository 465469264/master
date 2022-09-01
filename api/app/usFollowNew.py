from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
#直播间关注
class usFollowNew(HttpRunner):
    config = (
        Config("直播间关注讲师")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                "body": {
                                            "operateType": "$operateType",                            #1：新增关注 2：取消关注
                                            "targetUserId": "$targetUserId",                        #我需要关注对象的userId
                                        },
                                "header": {
                                    "appType": "3"
                                }
                            },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("直播间关注讲师")
            .post("/proxy/us/usFollowNew/1.0/")
            .with_headers(
                **{
                    "authtoken": "${ENV(app_auth_token)}",
                    "User-Agent": "yuan zhi jiao yu/7.19.6 (iPhone; iOS 12.5.5; Scale/3.00)",
                    "Content-Type": "text/yzedu+",
                    "Host":"${ENV(Host)}",
                    "Connection":"Keep-Alive"
                }
            )
            .with_data("$data")
            .extract()
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]

