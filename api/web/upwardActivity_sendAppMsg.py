from httprunner import HttpRunner, Config, Step, RunRequest

# APP活动管理提醒
class upwardActivity_sendAppMsg(HttpRunner):
    config = (
        Config("触发APP活动管理活动提醒")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("触发活动提")
                .post("/upwardActivity/sendAppMsg")
                .with_headers(**{
                "Accept":"*/*",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept-Encoding":"gzip, deflate, br",
                "Connection":"keep-alive",
                "Cookie": "$Cookie"
            })
                .with_data({"actId": "$actId","actName":"$actName"})
                .validate()
                .assert_equal("body.body", "success")
        )
    ]