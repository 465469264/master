#学服任务列表
from httprunner import HttpRunner, Config, Step, RunRequest
class studyActivity_list(HttpRunner):
    config = (
        Config("学服任务列表")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("学服任务列表")
                .get("/studyActivity/list.do")
                .with_headers(**
                                {
                                    "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                                    "Host": "${ENV(Host)}",
                                    "Cookie":"$Cookie"
                                }
                              )
                .with_params(start='0',length='10')
                .extract()
                .with_jmespath("body.body.data[0].taskId","taskId")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]