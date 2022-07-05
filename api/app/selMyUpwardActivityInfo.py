from httprunner import HttpRunner, Config, Step, RunRequest
#我的活动页
class selMyUpwardActivityInfo(HttpRunner):
    config = (
        Config("我的活动页")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                        "type": "$type",                     #1>报名中        2>进行中   3>已结束
                                        "pageSize": "$pageSize",                #尺寸
                                        "pageNum": "$pageNum"              #页码
                                    },
                                    "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("我的活动页")
                .post("/proxy/mkt/selMyUpwardActivityInfo/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "text/yzedu+",
                            "authtoken": "${ENV(app_auth_token)}",
                            "Host": "${ENV(app_Host)}"
                }
            )
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")

        )
    ]





if __name__ == '__main__':
    selMyUpwardActivityInfo().test_start()
