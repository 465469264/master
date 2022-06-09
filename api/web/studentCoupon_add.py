from httprunner import HttpRunner, Config, Step, RunRequest
#赠送优惠券
class studentCoupon_add(HttpRunner):
    config = (
        Config("赠送优惠券")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("赠送优惠券")
                .post("/studentCoupon/add.do")
                .with_headers(**{
                "Content - Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length": "246",
                "Host": "${ENV(Host)}",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Cookie": "$Cookie"
                            })
                .with_data(
                {
                    "learnId":"$learnId",
                    "couponId":"$couponId",
                    "reasonDesc":"$reasonDesc",
                    "stdId":"$stdId",
                    "remark":"$remark"
                }
                            )

                .validate()
                .assert_equal("status_code", 200)
        )
]