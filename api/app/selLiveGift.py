from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
#获取直播间的礼物赠送配置
class selLiveGift(HttpRunner):
    config = (
        Config("获取直播间的礼物赠送配置")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
            "number": {
                        "header": {
                            "appType": "4",
                        },
                        "body": {
                        }
                    },
            "data": "${base64_encode($number)}"
        })
    )
    teststeps = [
        Step(
            RunRequest("获取直播间的礼物赠送配置")
            .post("/proxy/mkt/selLiveGift/1.0/")
            .with_headers(
                **{
                    "authtoken": "${ENV(app_auth_token)}",
                    "Content-Type": "text/yzedu+; charset=UTF-8",
                }
            )
            .with_data('$data')
            .extract()
            .with_jmespath("body.body[0].money", "money")
            .with_jmespath("body.body[0].name", "gift_name")
            .with_jmespath("body.body[0].giftType", "giftType")
            .with_jmespath("body.body[0].id", "id")
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]


if __name__ == "__main__":
    selLiveGift().test_start()