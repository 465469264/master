#查询所有人
from httprunner import HttpRunner, Config, Step, RunRequest
class usFollowInfos(HttpRunner):
    config = (
        Config("查询所有人")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": { "header": {
                                        "appType": "4",
                                    },
                                    "body": {
                                                "pageSize": "$pageSize",
                                                "pageNum": "$pageNum",
                                                "keyWord": "$keyWord"                 #搜索关键词
                                    }
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("查询所有人")
                .post("/proxy/us/usFollowInfos/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.unFollowedInfos[0].realName","realName")
                .with_jmespath("body.body.unFollowedInfos[0].id","userId1")
                .with_jmespath("body.body.unFollowedInfos[1].realName","realName2")
                .with_jmespath("body.body.unFollowedInfos[1].id","userId2")
                .validate()
                .assert_equal("body.message", "$message")

        )
    ]

if __name__ == '__main__':
    usFollowInfos().test_start()