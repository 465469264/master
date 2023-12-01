from httprunner import HttpRunner, Config, Step, RunRequest
#删除评论
class DeleteComment(HttpRunner):
    config = (
        Config("删除评论")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                            "mappingId": "$mappingId",
                                            "id": "$comment_Id",
                                            "commentType": "$commentType",                 #评论业务 类型，1：咨询文章，2：上进故事 3：上进活动 4:圈子
                                            "timeStamp": "${timestap()}",
                                    },
                                        "header":{"appType":"${ENV(appType)}"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
    )
    teststeps = [
        Step(
            RunRequest("删除评论")
                .post("/proxy/mkt/deleteComment/1.0/")
                .with_headers(**{
                                    "User-Agent": "${ENV(User-Agent)}",
                                    "Content-Type": "text/yzedu+; charset=UTF-8",
                                    "Host": "${ENV(app_Host)}",
                                    "authtoken": "${ENV(app_auth_token)}",
                                    })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]

