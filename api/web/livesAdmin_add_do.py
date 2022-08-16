#后台新增管理员
from httprunner import HttpRunner, Config, Step, RunRequest
class livesAdmin_add(HttpRunner):
    config = (
        Config("新增房间管理员")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("后台新增管理员")
                .post("/livesAdmin/add.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"$Cookie"

    })
                .with_data({
                            "manageType": "$manageType",       #管理模块 对应字典  1>直播广场
                            "userId": "$userId",
                            "yzCode": "$yzCode",
                            "mobile": "$mobile",
                            "userName": "$userName"

                            }
                            )
                .extract()
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    livesAdmin_add().test_start()