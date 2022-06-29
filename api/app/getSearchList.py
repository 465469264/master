#组合搜索
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class getSearchList(HttpRunner):
    config = (
        Config("组合搜索")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                        "keyWords": "$keyWords",                  #搜索关键字
                                        "type": "$type"                  #类型，0>搜索栏搜索    6>上进学社   2>查询好友  7>查询老师  4>上进习惯  5>上进活动  3>查看话题  1>查看动态  8>礼品商城  12>上进直播
                                    },
                                    "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("组合搜索")
                .post("/proxy/search/getSearchList/1.0/")
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
    getSearchList().test_start()



