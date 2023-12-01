from httprunner import HttpRunner, Config, Step, RunRequest
# 带出书籍
class selUsNewBookDetail(HttpRunner):
    config = (
        Config("带出书籍")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                            "timeStamp": "${timestap()}"
                                    },
                                    "header": {"appType": "${ENV(appType)}"}
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
                "User-Agent": "${ENV(User-Agent)}",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            }
                              )
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.name","name")
                .with_jmespath("body.body.imgUrl","imgUrl")
                .with_jmespath("body.body.readPersonNum","readPersonNum")
                .with_jmespath("body.body.bookId","bookId")
                .validate()
                .assert_equal("body.message", "$message")

        )
    ]

if __name__ == '__main__':
    selUsNewBookDetail().test_start()