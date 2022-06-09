from httprunner import HttpRunner, Config, Step, RunRequest
#查询考前辅导费缴费列表
class querry(HttpRunner):
    config = (
        Config("查询辅导费")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("查询学员缴费管理的缴费学员")
                .post("/stdFee/list.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"${ENV(COOKIE)}"
            })
                .with_data({"mobile": "$mobile"})
                .extract()
                .with_jmespath("body.body.data[0].learnId", "learnId")
                .with_jmespath("body.body.data[0].learnId", "learn_Id")
                .with_jmespath("body.body.data[0].payInfos[0].subOrderNo", "subOrderNo")
                .with_jmespath("body.body.data[0].grade", "grade")
                .with_jmespath("body.body.data[0].payInfos[0].feeAmount", "feeAmount")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    querry().test_start()