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
                                        "activeName": "amylee成人教育课程活动",
                                        "pfsnLevelName": "1>专科升本科类",
                                        "android_phoneModel": "SM-N9500",
                                        "idCard": "$idCard",
                                        "recruitType": "1",
                                        "zmtoken": "$zmtoken",
                                        "android_version": "7.19.2",
                                        "android_sdk": 28,
                                        "unvsName": "amylee成人教育学校",
                                        "pfsnName": "amylee成人教育",
                                        "taName": "广州南沙",
                                        "CREATOR": {},
                                        "grade": "2022",
                                        "scholarship": "1273",
                                        "name": "$name",
                                        "pfsnLevel": "1",
                                        "unvsId": "164690457468960222",
                                        "pfsnId": "164690470996983675",
                                        "taId": "169"
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
                "authtoken": "$app_auth_token",
            })
                .with_data('$data')
                .validate()
                .assert_equal("status_code", 200)
        )
    ]

