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
            RunRequest("智米")
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
                            "userId": "$userId",
                            "zhimiType": "$zhimiType",                #1>进账   2>出账
                            "accSerialType": "$accSerialType",            #1>注册赠送  2>缴费送自身  3>下线缴费送  4>任务卡赠送  5>其他补送  26>其他收回	27>抽奖使用	28>活动报名
                            "zhimiCount":"$zhimiCount",
                            "reasonDesc":"测试",
                            }
                            )

                .validate()
                .assert_equal("status_code", 200)
        )
]