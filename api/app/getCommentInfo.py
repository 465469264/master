from httprunner import HttpRunner, Config, Step, RunRequest
#获取评论信息
class getCommentInfo(HttpRunner):
    config = (
        Config("获取评论信息")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                            "pageSize": "$pageSize",
                                            "sortOrder": "$sortOrder",        #排序方式  1按热度  2按时间
                                            "pageNum": "$pageNum",
                                            "mappingType": "$mappingType",               #评论业务 类型，1：咨询文章，2：上进活动 4:圈子
                                            "mappingId": "$mappingId"            #圈子id/活动id/习惯id
                                        },
                                        "header":{"appType":"4"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("获取评论信息")
                .post("/proxy/mkt/getCommentInfo/1.0/")
                .with_headers(**{
                            "User-Agent": "${ENV(User-Agent)}",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "${ENV(app_auth_token)}",
                                }
                                )
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.list[0].commentId", "commentId")
                .with_jmespath("body.body.list[0].mappingId", "mappingId")
                .with_jmespath("body.body.list[0].ifFabulous", "ifFabulous")      #提取是否点赞
                .with_jmespath("body.body.list","body")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    getCommentInfo().test_start()


