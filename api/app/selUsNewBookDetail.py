from httprunner import HttpRunner, Config, Step, RunRequest
# 带出书籍
class selUsNewBookDetail(HttpRunner):
    config = (
        Config("带出书籍")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                            "markTaskType": "$markTaskType",
                                        },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("带出书籍")
                .post("/proxy/us/selUsNewBookDetail/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.name","name")
                .with_jmespath("body.body.imgUrl","imgUrl")
                .with_jmespath("body.body.readPersonNum","readPersonNum")
                .with_jmespath("body.body.bookId","bookId")
                .validate()
                .assert_equal("body.message", "$message")
                # .assert_equal("body.body.name", "$name")

        )
    ]

if __name__ == '__main__':
    selUsNewBookDetail().test_start()