from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
#获取直播间信息，进直播间/主播退出直播间时调用
class liveInfos(HttpRunner):
    config = (
        Config("获取直播间信息")
            .base_url("${ENV(im)}")
            .verify(False)
            .variables(**{
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("获取直播间信息")
            .post("/proxy/im-mkt/live/liveInfos")
            .with_headers(
                **{
                    "User-Agent": "yuan zhi jiao yu/7.19.6 (iPhone; iOS 12.5.5; Scale/3.00)",
                    "Content-Type": "application/json",
                    "Host":"${ENV(im_host)}",
                    "Connection":"Keep-Alive"
                }
            )
            .with_json(
                        {"groupId": "$groupId",
                         "userId": "$userId"                 #进入直播间时身份人的对应userId
                         }
                        )
            .extract()
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]