from httprunner import HttpRunner, Config, Step, RunRequest

#查询学院订单
class querry2(HttpRunner):
    config = (
        Config("查询学院订单")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("查询学员")
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
                .with_jmespath("body.body.data[0].payInfos[1].subOrderNo", "subOrderNo1")
                .with_jmespath("body.body.data[0].payInfos[2].subOrderNo", "subOrderNo2")
                .with_jmespath("body.body.data[0].payInfos[3].subOrderNo", "subOrderNo3")
                .with_jmespath("body.body.data[0].payInfos[4].subOrderNo", "subOrderNo4")
                .with_jmespath("body.body.data[0].payInfos[5].subOrderNo", "subOrderNo5")
                .with_jmespath("body.body.data[0].payInfos[6].subOrderNo", "subOrderNo6")
                .with_jmespath("body.body.data[0].grade", "grade")
                .with_jmespath("body.body.data[0].payInfos[0].feeAmount", "feeAmount")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]