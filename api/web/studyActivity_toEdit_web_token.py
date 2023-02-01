from httprunner import HttpRunner, Config, Step, RunRequest
#获取新增/编辑学服任务的_web_token
class studyActivity_toEdit(HttpRunner):
    config = (
        Config("获取新增/编辑学服任务的_web_token")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("web_token")
            .get("/studyActivity/toEdit.do")
            .with_headers(**{
                            "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                            "Host": "${ENV(Host)}",
                            "Cookie":"$Cookie"
            })
            .with_params(exType='$exType')
            .extract()
            .with_jmespath("body","body")
            .validate()
            .assert_equal("status_code", 200)
        )
    ]