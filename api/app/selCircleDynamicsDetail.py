from httprunner import HttpRunner, Config, Step, RunRequest
#圈子详情
class selCircleDynamicsDetail(HttpRunner):
    config = (
        Config("获取圈子数据")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                        "id": "$id",   #圈子id

                                    },
                                    "header":{
                                            "appType": "3",
                                        }
                                },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("获取圈子数据")
                .post("/proxy/us/selCircleDynamicsDetail/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",

                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].id", "id")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    selCircleDynamicsDetail().test_start()