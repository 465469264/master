from httprunner import HttpRunner, Config, Step, RunRequest
#智米赠送
class zhimi_give(HttpRunner):
    config = (
        Config("智米赠送")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("智米赠送")
                .post("/zhimi_give/add.do")
                .with_headers(**{
                "Content - Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length": "246",
                "Host": "bms.yzwill.cn",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Cookie": "$Cookie"
                                }
                                )
                .with_data(
                            {
                            "_web_token": "$_web_token",
                            "userId": "$user_id",
                            "zhimiType": "1",
                            "accSerialType": "5",
                            "zhimiCount":"699",
                            "reasonDesc":"测试",
                            }
                            )

                .validate()
                .assert_equal("status_code", 200)
        )
]