#获取可报名的大学
from httprunner import HttpRunner, Config, Step, RunRequest
class RecruitUnvsList(HttpRunner):
    config = (
        Config("获取可报名的大学")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                      "header": {"appType": "2",
                                                 "deviceId": "AFE40300-BC49-4CEB-9825-951DA17100BE"},
                                       "body": {
                                                "pfsnLevel": "$pfsnLevel",           #5>高中起点高职高专	，1>专科升本科类 6>硕士研究生，7>中专，8>高起本
                                                "recruitType": "$recruitType",       #recruitType.1>成人教育 2>国家开放大学	3>全日制	 4>自考	5>硕士研究生  6>中专
                                                "cityCode": "$cityCode",           #城市编码
                                            }
                                        }
                                    ,
                          "data": "${base64_encode($number)}",
                          })
    )
    teststeps = [
        Step(
            RunRequest("获取可报名的大学")
                .post("/proxy/mkt/recruitUnvsList/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath('body.body[0].unvsId', 'unvsId')
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    RecruitUnvsList().test_start()