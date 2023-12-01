#习惯帖子列表
from httprunner import HttpRunner, Config, Step, RunRequest
class SocialCircle_habitList(HttpRunner):
    config = (
        Config("习惯帖子列表")
            .base_url("${ENV(yzjy-app)}")
            .verify(False)
            .variables(**{
                        "number": {
                            "data": {
                                    "pageNum": "$pageNum",
                                    "taskId": "$taskId",
                                    "userRoleType": "$userRoleType",
                                    "scType": "$scType",                        #11 => 习惯-打卡记录
                                    "pageSize": "$pageSize",
                                    },
                            "client": {
                                    "platform": "${ENV(platform)}",
                                    "appVersion": "${ENV(appVersion)}",
                                    "systemVersion": "${ENV(systemVersion)}"
                                        }
                                    }
                            }
                       )
                            )
    teststeps = [
        Step(
            RunRequest("习惯帖子列表")
                .post("/proxy/bbs-server/socialCircle/habitList/")
                .with_headers(**{
                "User-Agent": "${ENV(User-Agent)}",
                "appType": "${ENV(appType)}",
                "Content-Type": "application/json",
                "Accept-Encoding":"gzip, deflate, br",
                "Host": "${ENV(yzjy-app-Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                                }
                              )
                .with_json("$number")
                .extract()
                .with_jmespath("body.data[0].id", "id")         #帖子id
                .validate()
                .assert_equal("body.state.msg", "$msg")

        )
    ]