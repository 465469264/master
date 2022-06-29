from httprunner import HttpRunner, Config, Step, RunRequest
#点赞活动
class usPraise(HttpRunner):
    config = (
        Config("点赞")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                        "fabulousNum": "$fabulousNum",        #点赞数量  1>点赞  -1>取消点赞
                                        "praiseType": "$praiseType",          #点赞类型	2>活动点赞    3>圈子       5>点赞评论
                                        "praiseId": "$praiseId",              #圈子帖子/活动id
                                        },
                                        "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("点赞")
                .post("/proxy/us/usPraise/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "${ENV(app_auth_token)}",

            }
            )
                .with_data('$data')
                .validate()
                .assert_equal("body.message", "success")
        )
    ]
if __name__ == '__main__':
    usPraise().test_start()


