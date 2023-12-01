#获取可报读专业

from httprunner import HttpRunner, Config, Step, RunRequest
class EnrollInfo_pfsnName(HttpRunner):
    config = (
        Config("报读页面-根据选择的院校-获取可报读专业")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                      "header": {"appType": "4",
                                                 },
                                       "body": {
                                           "unvsId": "$unvsId",               #院校id
                                           "pageSize": "$pageSize",
                                           "pageNum": "$pageNum",
                                           "scholarship": "$scholarship",       #优惠类型--前端写死
                                           "grade": "$grade",                    #报读年级-前端写死
                                           "unvsName": "$unvsName",            #大学名称
                                           "type": "P",                       #P:获取专业的传值
                                           "pfsnLevel": "$pfsnLevel"          #专业层次
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
                .with_jmespath("body.body[0].pfsnName", "pfsnName")
                .with_jmespath("body.body[0].pfsnId", "pfsnId")
                .with_jmespath("body.body[0].pfsnCode", "pfsnCode")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
