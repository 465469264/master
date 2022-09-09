#建立消息通道
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

class instance(HttpRunner):
    config = (
        Config("建立消息通道")
            .base_url("${ENV(im)}")
            .verify(False)
            .variables(**{
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("建立消息通道")
            .get("/proxy/instance/1.0/")
            .with_headers(
                **{
                    "User-Agent": "yuan zhi jiao yu/7.19.6 (iPhone; iOS 12.5.5; Scale/3.00)",
                    "Content-Type": "application/json",
                    "Host":"${ENV(im_host)}",
                    "Connection":"Keep-Alive"
                }
            )
            .with_json({
                    })
            .extract()
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]