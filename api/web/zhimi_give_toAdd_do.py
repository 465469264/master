from httprunner import HttpRunner, Config, Step, RunRequest
#获取智米赠送的web_token
class zhimi_token(HttpRunner):
    config = (
        Config("取智米赠送的web_token")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("web_token")
                .post("/zhimi_give/toAdd.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Host": "${ENV(Host)}",
                "Cookie":"$Cookie"
            })
                .extract()
                .with_jmespath("body","body")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]