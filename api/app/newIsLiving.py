#2022-12-1-----一个新的获取正在直播数量的直播接口
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class newIsLiving(HttpRunner):
    config = (
        Config("获取正在直播数量的直播接口")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
            "number": {
                "body": {
                        "android_sdk": 28,

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
            RunRequest("获取正在直播数量的直播接口")
            .post("/proxy/us/newIsLiving/1.0/")
            .with_headers(
                **{
                    "authtoken": "${ENV(app_auth_token)}",
                    "User-Agent": "Android/environment=test/app_version=7.19.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                    "Content-Type": "text/yzedu+; charset=UTF-8",
                }
            )
            .with_data('$data')
            .extract()
            .with_jmespath("body.body.isLiving", "isLiving")
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]


if __name__ == "__main__":
    isLiving().test_start()