from httprunner import HttpRunner, Config, Step, RunRequest

# 获取webtoken
class web_token(HttpRunner):
    config = (
        Config("获取webtoken")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("获取webtoken")
                .post("/stdFee/toPay.do")
                .with_headers(**{
                "Accept":"*/*",
                "User-Agent":"PostmanRuntime/7.28.4",
                "Accept-Encoding":"gzip, deflate, br",
                "Connection":"keep-alive",
                "Cookie": "$Cookie"
            })
                .with_data({"learnId": "$learnId"})
                .extract()
                .with_jmespath("body","body") #获取body
        )
    ]