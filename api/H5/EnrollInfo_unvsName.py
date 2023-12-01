#报读页面-可报读的院校

from httprunner import HttpRunner, Config, Step, RunRequest
class EnrollInfo_unvsName(HttpRunner):
    config = (
        Config("报读页面-可报读的院校")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                      "header": {"appType": "4",
                                                 },
                                       "body": {
                                                "type": "U",                      #U：请求院校
                                                "scholarship": "$scholarship",    #优惠类型--前端写死
                                                "grade": "$grade",                 #报读年级-前端写死
                                                "pageSize": "$pageSize",
                                                "pageNum": "$pageNum",


                                       }
                                        }
                                    ,
                          "data": "${base64_encode($number)}",
                          })
    )
    teststeps = [
        Step(
            RunRequest("报读页面-可报读的院校")
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
                .with_jmespath("body.body[0].unvsCode", "unvsCode")
                .with_jmespath("body.body[0].unvsId", "unvsId")
                .with_jmespath("body.body[0].unvsName", "unvsName")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
