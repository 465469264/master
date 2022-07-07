#上进分-等级列表
from httprunner import HttpRunner, Config, Step, RunRequest
class advLevelList(HttpRunner):
    config = (
        Config("上进分-等级列表")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                        "minLevel": "$minLevel",        #显示的最低范围
                                        "maxLevel": "$maxLevel",        #显示的最高范围
                                        },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("上进分-等级列表")
                .post("/proxy/mkt/advLevelList/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")

        )
    ]

if __name__ == '__main__':
    sign().test_start()