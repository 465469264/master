#获取报读页面的banner图
from httprunner import HttpRunner, Config, Step, RunRequest
class GetMarketingBanner(HttpRunner):
    config = (
        Config("获取成人教育的branna图")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                      "header": {"appType": "2",
                                                 "deviceId": "AFE40300-BC49-4CEB-9825-951DA17100BE"},
                                       "body": {
                                                   "type": "$type",                  #"type": "8", "type": ck_7 >>都是H5写死的
                                                   "bannerBelong": "$bannerBelong",          #"bannerBelong": 1, "bannerBelong": 2,>>都是H5写死的
                                            }
                                        }
                                    ,
                          "data": "${base64_encode($number)}",
                          })
    )
    teststeps = [
        Step(
            RunRequest("获取成人教育的branna图")
                .post("/proxy/sys/getMarketingBanner/1.0/")
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
    GetMarketingBanner().test_start()