from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
#管理员获取全部观众
class selWatchRecord(HttpRunner):
    config = (
        Config("管理员获取全部观众")
            .base_url("${ENV(im)}")
            .verify(False)
            .variables(**{
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("管理员获取全部观众")
            .post("/proxy/im-user/user/selWatchRecord")
            .with_headers(
                **{
                    "User-Agent": "yuan zhi jiao yu/7.19.6 (iPhone; iOS 12.5.5; Scale/3.00)",
                    "Content-Type": "application/json",
                    "Host":"${ENV(im_host)}",
                    "Connection":"Keep-Alive"
                }
            )
            .with_json(
                        {
                            "pageSize": "100",
                            "groupId": "$groupId",
                            "pageNum": "1"
                        }
                        )
            .extract()
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]