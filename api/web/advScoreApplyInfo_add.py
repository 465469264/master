from httprunner import HttpRunner, Config, Step, RunRequest

#赠送上进分
class advScoreApplyInfo(HttpRunner):
    config = (
        Config("赠送上进分")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("赠送上进分")
                .post("/advScoreApplyInfo/add.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"${ENV(COOKIE)}"
            })
                .with_data(
                            # {
                            # # "exType": "$exType",          #ADD>赠送
                            # # "userId": "$userId",
                            # # "scoreType":"$scoreType",     #1>增分
                            # "score": "$score",
                            # "reason": "$reason"
                            # }
                            {
                                "exType": "ADD",
                                "userId": "113639",
                                "scoreType": "1",
                                "score": "80000",
                                "reason": "测试"
                            }
                            )
                .extract()
                .validate()
                .assert_equal("status_code", 200)
        )
    ]

if __name__ == '__main__':
    advScoreApplyInfo().test_start()