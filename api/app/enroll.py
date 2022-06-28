from httprunner import HttpRunner, Config, Step, RunRequest
#报名成教
class sign_up_education(HttpRunner):
    config = (
        Config("报名成教")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{

                          "number": {
                              "body": {
                                        "activeName": "$activeName",         #营销活动
                                        "pfsnLevelName": "$pfsnLevelName",    #报考层次
                                        "idCard": "$idCard",
                                        "recruitType": "$recruitType",
                                        "zmtoken": "$zmtoken",
                                        "unvsName": "$unvsName",            #院校名字
                                        "pfsnName": "$pfsnName",            #专业名称
                                        "taName": "$taName",                #考区名字
                                        "CREATOR": {},
                                        "grade": "$grade",                 #报读年级
                                        "scholarship": "$scholarship",     #优惠类型
                                        "name": "$name",                   #学生名字
                                        "pfsnLevel": "$pfsnLevel",        #专业层次
                                        "unvsId": "$unvsId",             #院校id
                                        "pfsnId": "$pfsnId",             #专业id
                                        "taId": "$taId"                   #考区id
                                    },
                              "header": {"appType": "3"}
                          },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("报名成教")
                .post("/proxy/mkt/enroll/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .validate()
                .assert_equal("status_code", 200)
        )
    ]

