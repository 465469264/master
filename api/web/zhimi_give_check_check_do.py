from httprunner import HttpRunner, Config, Step, RunRequest
#审核智米赠送
class check_zhimi(HttpRunner):
    config = (
        Config("智米赠送审核")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("智米赠送审核")
                .post("/zhimi_give_check/check.do")
                .with_headers(**{
                "Content - Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Host": "bms.yzwill.cn",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Cookie": "$Cookie",
                "transferSeq": "1",
                "X-Requested-With": "XMLHttpRequest",
                "uri":"http://bms.yzwill.cn/zhimi_give_check/toCheck.do?id=$id"
                                }
                                )
                .with_data(
                {
                    "id": "$id",
                    "reasonStatus": "$reasonStatus",       #2>通过   3>驳回
                    "rejectDesc": "",
                    "_web_token": "$_web_token",
                }
            )

                .validate()
                .assert_equal("status_code", 200)
        )
]