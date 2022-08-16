#改变管理员状态
from httprunner import HttpRunner, Config, Step, RunRequest
class livesAdmin_update(HttpRunner):
    config = (
        Config("改变管理员状态")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("改变管理员状态")
                .post("/livesAdmin/update.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"$Cookie"

    })
                .with_data({
                            "id": "$id",                      #id:
                            "isAllow": "$isAllow"             #1>启用  2>禁用
                            }
                            )
                .extract()
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    livesAdmin_update().test_start()