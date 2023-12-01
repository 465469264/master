#获取报读专业接口
from httprunner import HttpRunner, Config, Step, RunRequest
class findPfsnByActId(HttpRunner):
    config = (
        Config("获取报读专业接口")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                      "header": {"appType": "2",
                                                 "deviceId": "AFE40300-BC49-4CEB-9825-951DA17100BE"},
                                       "body": {
                                               "actId": "$actId",                   #营销活动配置id~！！！这是是前端写死的
                                               "pfsnLevel": "$pfsnLevel",           #5>高中起点高职高专	，1>专科升本科类 6>硕士研究生，7>中专，8>高起本
                                               "pfsnName": "$pfsnName",             #专业名称
                                            }
                                        }
                                    ,
                          "data": "${base64_encode($number)}",
                          })
    )

    teststeps = [
        Step(
            RunRequest("获取报读专业")
                .post("/proxy/mkt/findPfsnByActId/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].pfsnName", "pfsnName")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    findPfsnByActId().test_start()
