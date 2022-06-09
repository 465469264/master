from httprunner import HttpRunner, Config, Step, RunRequest
#获取收费审核列表
class feeReview_list(HttpRunner):
    config = (
        Config("查找缴费审核学员")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("查找缴费审核学员")
                .post("/feeReview/list.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"${ENV(COOKIE)}"
            })
                .with_data({"mobile": "$mobile"})
                .extract()
                .with_jmespath("body.body.data[0].subOrderNo", "subOrderNo1")
                .with_jmespath("body.body.data[1].subOrderNo", "subOrderNo2")
                .with_jmespath("body.body.data[2].subOrderNo", "subOrderNo3")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]