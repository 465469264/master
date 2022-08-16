from httprunner import HttpRunner, Config, Step, RunRequest

#获取用户信息，获取userId
class getUserInfo(HttpRunner):
    config = (
        Config("获取用户信息，获取userId")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("获取用户信息，获取userId")
                .get("/zhimi_give/getUserInfo.do?sName=$mobile")
                .with_headers(**{
                "Content - Type": "application/json;charset=UTF-8",
                "Referer":"http://bms.yzwill.cn/zhimi_give/toAdd.do",
                "X-Requested-With":"XMLHttpRequest",
                "Host": "${ENV(Host)}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Cookie": "$Cookie"
                                }
                            )
                .extract()
                .with_jmespath("body.body.data[0].user_id", "user_id")
                .with_jmespath("body.body.data[0].yz_code", "yz_code")
                .with_jmespath("body.body.data[0].real_name", "real_name")
                .validate()
                .assert_equal("status_code", 200)
        )
]