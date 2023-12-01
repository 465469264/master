#邀约有礼页面-当前账号的邀约记录

from httprunner import HttpRunner, Config, Step, RunRequest
class GetUsInviteRecord(HttpRunner):
    config = (
        Config("邀约有礼页面-当前账号的邀约记录")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                      "header": {"appType": "2",
                                                 "deviceId": "AFE40300-BC49-4CEB-9825-951DA17100BE"},
                                       "body": {

                                            }
                                        }
                                    ,
                          "data": "${base64_encode($number)}",
                          })
    )

    teststeps = [
        Step(
            RunRequest("邀约有礼页面-当前账号的邀约记录")
                .post("/proxy/us/getUsInviteRecord/1.0/")
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
    GetUsInviteRecord().test_start()
