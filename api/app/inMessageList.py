from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
#消息中心>进入@我，点赞，评论,粉丝
# 8>@我   9>点赞   10>评论  ,11>粉丝
class inMessageList(HttpRunner):
    config = (
        Config("消息中心>进入@我，点赞，评论,粉丝")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
            "number": {
                "body": {
                        "msgType": "$msgType",
                        "pageSize":"$pageSize",
                        "pageNum": "$pageNum"
                        },
                "header": {
                    "appType": "3"
                }
            },
            "data": "${base64_encode($number)}"
        })
    )
    teststeps = [
        Step(
            RunRequest("消息中心>进入@我，点赞，评论,粉丝")
            .post("/proxy/bds/inMessageList/1.0/")
            .with_headers(
                **{
                    "authtoken": "${ENV(app_auth_token)}",
                    "User-Agent": "Android/environment=test/app_version=7.19.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                    "Content-Type": "text/yzedu+; charset=UTF-8",
                }
            )
            .with_data('$data')
            .extract()
            .with_jmespath('body.body[0].msgTitle','msgTitle')
            .validate()
            .assert_equal("body.message", "$message")
            .assert_equal('body.body[0].msgTitle','$msgTitle')

        ),
    ]


if __name__ == "__main__":
    inMessageList().test_start()