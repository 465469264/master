from httprunner import HttpRunner, Config, Step, RunRequest
#查询智米审核列表,获取要审核的记录id
class zhimi_give_check_list(HttpRunner):
    config = (
        Config("智米赠送审核列表")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("获取要审核的记录id")
                .post("/zhimi_give_check/list.do")
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
                            "mobile": "$mobile",
                            }
                            )
                .extract()
                .with_jmespath("body.body.data[0].id", "id")
                .validate()
                .assert_equal("status_code", 200)
        )
]