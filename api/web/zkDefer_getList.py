from httprunner import HttpRunner, Config, Step, RunRequest
#自考延长考期跟进
class zkDefer_getList(HttpRunner):
    config = (
        Config("自考延长考期跟进")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("自考延长考期跟进")
                .post("/zkDefer/getList.do")
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
                            "length": "10",
                            "start": "0",
                            "stdName": "$stdName",     #学员姓名查询
                            "ifApplyDelay": "$ifApplyDelay"        #是否延期  Y>是   N>不是

                            }
                            )
                .extract()
                .with_jmespath("body.body.data[0].learnId","learnId")
                .validate()
                .assert_equal("status_code", 200)
        )
]