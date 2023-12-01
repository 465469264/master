#报读页面-根据选择的院校-选择可选层次

from httprunner import HttpRunner, Config, Step, RunRequest
class EnrollInfo_pfsnLevelName(HttpRunner):
    config = (
        Config("报读页面-根据选择的院校-选择可选层次")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                      "header": {"appType": "4",
                                                 },
                                       "body": {
                                           "pfsnId": "7089549895656277197",
                                           "unvsId": "$unvsId",
                                           "pageNum": "$pageNum",
                                           "scholarship": "$scholarship",           #优惠类型--前端写死
                                           "type": "L",                             #L：请求专业
                                           "pfsnLevel": "$pfsnLevel",               # 5>高中起点高职高专	，1>专科升本科类 6>硕士研究生，7>中专，8>高起本
                                           "unvsName": "$unvsName",
                                           "grade": "$grade",
                                           "pageSize": "$pageSize"
                                       }
                                        }
                                    ,
                          "data": "${base64_encode($number)}",
                          })
    )
    teststeps = [
        Step(
            RunRequest("报读页面-根据选择的院校-选择可选层次")
                .post("/proxy/mkt/enrollInfo/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                "Cookie": "$Cookie"
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].pfsnLevelName", "pfsnLevelName")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
