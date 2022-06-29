from httprunner import HttpRunner, Config, Step, RunRequest
#获取修改branner的 webtoken
class toBannerEdit_webtoken(HttpRunner):
    config = (
        Config("获取修改branner的 webtoken")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("获取修改branner的 webtoken")
                .post("/circleDynamic/toBannerEdit.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Host": "${ENV(Host)}",
                "Cookie":"$Cookie"
            })
                .with_data({"bannerId": "$bannerId"})
                .extract()
                .with_jmespath("body","body")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]