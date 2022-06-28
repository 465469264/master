from httprunner import HttpRunner, Config, Step, RunRequest
#评论帖子
class addNewComment(HttpRunner):
    config = (
        Config("评论")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                            "mappingId": "$mappingId",
                                            "ifLimit": "$ifLimit",          #搜当前业务是否支持多次评论，0：支持，1 不支持索类型
                                            "stdName": "$stdName",
                                            "nickName": "$nickname",
                                            "content": "$content",
                                            "realName": "$realName",
                                            "commentType": "$commentType",        #评论业务 类型，1：咨询文章，2：上进故事 3：上进活动 4:圈子
                                            "circleUserId": "$circleUserId",
                                            "notityList": "[{\"mobile\":\"$mobile\",\"userId\":\"$userId\",\"userName\":\"$userName\"}]",    #@人信息json字符串
                                        },
                                        "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("评论帖子")
                .post("/proxy/mkt/addNewComment/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "${ENV(app_auth_token)}",

            }
            )
                .with_data('$data')
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    addNewComment().test_start()


