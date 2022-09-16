#自考延长考期跟进------老师操作学员延期
from httprunner import HttpRunner, Config, Step, RunRequest
class zkDefer_applyDelay(HttpRunner):
    config = (
        Config("自考延长考期跟进------老师操作学员延期")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("自考延长考期跟进------老师操作学员延期")
            .post("/zkDefer/applyDelay.do")
            .with_headers(**{
                                "Content - Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                "Content - Length": "246",
                                "Host": "${ENV(Host)}",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                                "Cookie": "$Cookie"
                                }
                            )
            .with_data(
                        {
                        "learnId": "$learnId",                 #查看目标学员的延期记录
                        "applyServiceTimeEnd": "$applyServiceTimeEnd",
                        "remark":""
                        }
                        )
            .extract()
            .validate()
            .assert_equal("status_code", 200)
        )
]