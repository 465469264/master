#关注列表，根据userid
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class  SelMyCircleFollowList(HttpRunner):
    config = (
        Config("关注列表")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                        "pageSize": 20,
                                        "targetMobile": "$targetMobile",                        #对象手机
                                        "userId": "$userId",                       #关注列表的userid
                                        "targetRealName": "$targetRealName",        #对象名称
                                        "pageNum": 1                          #页码
                                    },
                                    "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("关注列表")
                .post("/proxy/us/selMyCircleFollowList/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "${ENV(app_auth_token)}",
                }
            )
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].targetUserId", "targetUserId")
                .with_jmespath("body.body[0].targetRealName", "targetRealName")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]

if __name__ == "__main__":
    SelMyCircleFollowList().test_start()



