from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
#直播间点赞
class livePraise(HttpRunner):
    config = (
        Config("直播间点赞")
            .base_url("${ENV(im)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("直播间点赞")
            .post("/proxy/im-mkt/live/livePraise")
            .with_headers(
                **{
                    "User-Agent": "yuan zhi jiao yu/7.19.6 (iPhone; iOS 12.5.5; Scale/3.00)",
                    "Content-Type": "application/json",
                    "Connection":"Keep-Alive"
                }
            )
            .with_json({
                        "userId": "$userId",
                        "groupId": "$groupId",
                        "praiseNum": "1"
                        }
                        )
            .extract()
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]

