#获取考试县区
from httprunner import HttpRunner, Config, Step, RunRequest
class EnrollInfo_taName(HttpRunner):
    config = (
        Config("报读页面-根据选择的院校-获取考试县区")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                      "header": {"appType": "4",
                                                 },
                                       "body": {
                                           "pfsnId": "$pfsnId",              #专业id
                                           "taName": "$taName",               #城市名称
                                           "unvsId": "$unvsId",                #院校id
                                           "pageNum": "$pageNum",
                                           "scholarship": "$scholarship",         #优惠类型--前端写死
                                           "type": "T",                         #T：考试县区
                                           "cityCode": "$cityCode",            #城市id
                                           "pfsnLevel": "$pfsnLevel",           #专业层次
                                           "unvsName": "$unvsName",            #院校id
                                           "grade": "$grade",                 #报读年级-前端写死
                                           "pageSize": "$pageSize"
                                       }
                                        }
                                    ,
                          "data": "${base64_encode($number)}",
                          })
    )
    teststeps = [
        Step(
            RunRequest("报读页面-根据选择的院校-获取考试县区")
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
                .with_jmespath("body.body[0].taId", "taId")
                .with_jmespath("body.body[0].taName", "taName")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
