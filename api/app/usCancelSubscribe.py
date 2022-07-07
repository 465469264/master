#习惯打卡-我的战绩里-开启/关闭打卡提醒
from httprunner import HttpRunner, Config, Step, RunRequest
class usCancelSubscribe(HttpRunner):
    config = (
        Config("习惯打卡-我的战绩里-开启/关闭打卡提醒")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                            "status": "$status"              #0>关闭    1>打开

                                            },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("习惯打卡-我的战绩里-开启/关闭打卡提醒")
                .post("/proxy/mkt/usCancelSubscribe/1.0/")
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
    usCancelSubscribe().test_start()