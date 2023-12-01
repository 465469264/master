#报读
from httprunner import HttpRunner, Config, Step, RunRequest
class Enroll(HttpRunner):
    config = (
        Config("报读")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                      "header": {"appType": "4",
                                                 },
                                       "body": {
                                           "pfsnId": "$pfsnId",              #专业id
                                           "taName": "$taName",              #考试县区名称
                                           "unvsId": "$unvsId",              #院校id
                                           "scholarship": "$scholarship",    #优惠类型--前端写死
                                           "recruitType": "$recruitType",    #recruitType.1>成人教育 2>国家开放大学	3>全日制	 4>自考	5>硕士研究生  6>中专
                                           "taId": "$taId",                  #考试县区id
                                           "idCard": "$idCard",              #身份证
                                           "pfsnName": "$pfsnName",          #报读专业
                                           "pfsnLevel": "$pfsnLevel",        #专业层次
                                           "unvsName": "$unvsName",          #院校id
                                           "grade": "$grade",                #报读年级-前端写死
                                           "name": "$name",
                                       }
                                        }
                                    ,
                          "data": "${base64_encode($number)}",
                          })
    )
    teststeps = [
        Step(
            RunRequest("报读")
                .post("/proxy/mkt/enroll/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "$app_auth_token",
                # "Cookie": "$Cookie"
            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
