from httprunner import HttpRunner, Config, Step, RunRequest
#评论
class AddNewComment(HttpRunner):
    config = (
        Config("评论")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                            "mappingId": "$mappingId",
                                            "picUrl": "$picUrl",                   #上传的配图路径
                                            "targetUserId": "$targetUserId",       #回复的时候对应的 被回复人id
                                            "ifLimit": "$ifLimit",                 #搜当前业务是否支持多次评论，0：支持，1 不支持索类型
                                            "stdName": "$stdName",
                                            "nickName": "$$realName",
                                            "content": "$content",
                                            "realName": "$realName",
                                            "commentType": "$commentType",        #评论业务 类型，1：咨询文章，2：上进故事 3：上进活动 4:圈子
                                            "circleUserId": "$circleUserId",      #被评论人的userid
                                        },
                                        "header":{"appType":"${ENV(appType)}"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("评论")
                .post("/proxy/mkt/addNewComment/1.0/")
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
if __name__ == '__main__':
    AddNewComment().test_start()


