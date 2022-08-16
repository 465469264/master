#直播列表
from httprunner import HttpRunner, Config, Step, RunRequest
class livesManage_list(HttpRunner):
    config = (
        Config("直播列表")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("直播列表")
                .post("/livesManage/list.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"$Cookie"

    })
                .with_data({
                            "start": "0",
                            "length": "10"
                            }
                            )
                .extract()
                # .with_jmespath("body.body.data[0].id", "id")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    livesManage_list().test_start()