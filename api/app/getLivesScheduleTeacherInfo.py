from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
#获取讲师信息
class getLivesScheduleTeacherInfo(HttpRunner):
    config = (
        Config("获取讲师信息")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
            "number": {
                        "header": {
                            "appType": "4",
                        },
                        "body": {
                            "timeStamp": "1660810887820",
                            "sign": "A16EBA65027E0054B0BE9003C655F425",
                            "mobile": "18565543603",
                            "liveId": "$liveId",
                            "userId": "$userId",
                            "iOS_version": "7.19.6"

                        }
                    },
            "data": "${base64_encode($number)}"
        })
    )
    teststeps = [
        Step(
            RunRequest("获取讲师信息")
            .post("/proxy/us/getLivesScheduleTeacherInfo/1.0/")
            .with_headers(
                **{
                    "authtoken": "${ENV(app_auth_token)}",
                    "Content-Type": "text/yzedu+; charset=UTF-8",
                    "User-Agent": "yuan zhi jiao yu/7.19.6 (iPhone; iOS 15.3.1; Scale/3.00)"
                }
            )
            .with_data('$data')
            .extract()
            .with_jmespath("body.body.userId", "teacher_userId")
            .with_jmespath("body.body.userName", "teacher_userName")
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]


if __name__ == "__main__":
    getLivesScheduleTeacherInfo().test_start()