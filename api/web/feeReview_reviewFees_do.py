from httprunner import HttpRunner, Config, Step, RunRequest
#批量审核
class reviewFee1(HttpRunner):
    config = (
        Config("收费审核")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("收费审核")
                .post("/feeReview/reviewFees.do")
                .with_headers(**{
                "Cookie":"${ENV(COOKIE)}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "uri": "http://bms.yzwill.cn/feeReview/toList.do",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With": "XMLHttpRequest",
            })
                # .with_json(dict(data=dict(subOrderNo=164972911469025733,learnId=164972911455470026)))
                .with_data(
                {
                    "data": '[{"subOrderNo":"$subOrderNo1","learnId":"$learnId"},{"subOrderNo":"$subOrderNo2","learnId":"$learnId"},{"subOrderNo":"$subOrderNo3","learnId":"$learnId"}]'
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        )
    ]