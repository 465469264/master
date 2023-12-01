#报读大学详情
from httprunner import HttpRunner, Config, Step, RunRequest
class UnvsDetail(HttpRunner):
    config = (
        Config("获取报读大学详情")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                      "header": {"appType": "2",
                                                 "deviceId": "AFE40300-BC49-4CEB-9825-951DA17100BE"},
                                       "body": {
                                                "pfsnLevel": "$pfsnLevel",           #5>高中起点高职高专	，1>专科升本科类 6>硕士研究生，7>中专，8>高起本
                                                "unvsId": "$unvsId",                 #院校id
                                            }
                                        }
                                    ,
                          "data": "${base64_encode($number)}",
                          })
    )
    teststeps = [
        Step(
            RunRequest("获取可报名的大学")
                .post("/proxy/mkt/unvsDetail/1.0/")
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
