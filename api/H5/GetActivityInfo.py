#获取优惠类型

from httprunner import HttpRunner, Config, Step, RunRequest
class GetActivityInfo(HttpRunner):
    config = (
        Config("获取报读页面-获取优惠类型")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                      "header": {"appType": "2",
                                                 "deviceId": "AFE40300-BC49-4CEB-9825-951DA17100BE"},
                                       "body": {
                                                "scholarship": "$scholarship",
                                                }
                                        },
                          "data": "${base64_encode($number)}",
                          })
    )
    teststeps = [
        Step(
            RunRequest("获取报读页面-营销活动信息")
                .post("/proxy/mkt/getActivityInfo/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("headers", "headers")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
