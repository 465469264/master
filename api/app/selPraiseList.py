from httprunner import HttpRunner, Config, Step, RunRequest
# 查看帖子的点赞列表
class SelPraiseList(HttpRunner):
    config = (
        Config("查看帖子的点赞列表")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                            "id": "id",
                                            "pageSize": "$pageSize",
                                            "pageNum": "$pageNum"
                                    },
                                    "header": {"appType": "${ENV(appType)}"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("查看帖子的点赞列表")
                .post("/proxy/us/selPraiseList/1.0/")
                .with_headers(**{
                                    "User-Agent": "${ENV(User-Agent)}",
                                    "Content-Type": "text/yzedu+; charset=UTF-8",
                                    "Host": "${ENV(app_Host)}",
                                    "authtoken": "${ENV(app_auth_token)}",
                                    }
                              )
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")

        )
    ]
