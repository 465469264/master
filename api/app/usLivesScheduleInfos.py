from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
#获取直播广场列表
class TestZhibo(HttpRunner):
    config = (
        Config("获取直播广场列表")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
            "number": {
                "body": {
                        "tab": "1",
                        "pageSize": "20",
                        "android_sdk": 28,
                        "userId": "$userId",
                        "pageNum": "1"
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
            RunRequest("获取直播广场列表")
            .post("/proxy/us/usLivesScheduleInfos/1.0/")
            .with_headers(
                **{
                    "authtoken": "${ENV(app_auth_token)}",
                    "User-Agent": "Android/environment=test/app_version=7.19.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                    "Content-Type": "text/yzedu+; charset=UTF-8",
                }
            )
            .with_data('$data')
            .extract()
            .with_jmespath("body.body[0].posterUrl", "posterUrl")
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]


if __name__ == "__main__":
    TestZhibo().test_start()