#添加学服任务的目标学员
from httprunner import HttpRunner, Config, Step, RunRequest
class task_addStu(HttpRunner):
    config = (
        Config("学服任务添加目标学员")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("学服任务添加目标学员")
                .post("/task/addStu.do")
                .with_headers(**
                                {
                                    "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                                    "Host": "${ENV(Host)}",
                                    "Cookie":"$Cookie"
                                }
                              )
                .with_data(
                            {
                                'idArray[]': '$learnId',              #学员的learnid
                                'taskId': '$taskId',
                                'taskTemplateType': '1',
                                'operType': '1'
                            }
            )
                .extract()
                .validate()
                .assert_equal("status_code", 200)
        )
    ]