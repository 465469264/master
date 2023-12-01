#可报读的城市
from httprunner import HttpRunner, Config, Step, RunRequest
class RecruitCityList(HttpRunner):
    config = (
        Config("可报读的城市")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                        "header": {"appType": "${ENV(appType)}"},

                                        "body": {
                                               "pfsnLevel": "$pfsnLevel",   # 5>高中起点高职高专	，1>专科升本科类 6>硕士研究生，7>中专，8>高起本
                                               "recruitType": "$recruitType", # recruitType.1>成人教育 2>国家开放大学	3>全日制	 4>自考	5>硕士研究生  6>中专
                                               "cityCode": "$cityCode",     # 城市编码
                                            }
                                        }
                                    ,
                          "data": "${base64_encode($number)}",
                          })
    )

    teststeps = [
        Step(
            RunRequest("可报读的城市")
                .post("/proxy/mkt/recruitCityList/1.0/")
                .with_headers(**{
                                    "User-Agent": "${ENV(User-Agent)}",
                                    "Content-Type": "text/yzedu+; charset=UTF-8",
                                    "Host": "${ENV(app_Host)}",
                                    "authtoken": "${ENV(app_auth_token)}",
                                    }
                              )
                .with_data('$data')
                .extract()
                .with_jmespath('body.body[0].cityCode', 'cityCode')
                .with_jmespath('body.body[0].cityCode', 'cityName')
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    RecruitCityList().test_start()
