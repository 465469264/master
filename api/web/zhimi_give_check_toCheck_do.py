from httprunner import HttpRunner, Config, Step, RunRequest
#获取智米审核web_token
class zhimi_check_token(HttpRunner):
    config = (
        Config("获取智米审核web_token")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("查询学员")
                .post("/zhimi_give_check/toCheck.do?id=$id")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Host": "bms.yzwill.cn",
                "Cookie":"$Cookie"
            })
                .extract()
                .with_jmespath("body","body")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]