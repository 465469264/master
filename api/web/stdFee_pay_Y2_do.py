from httprunner import HttpRunner, Config, Step, RunRequest

#缴学院订单Y2
class pay_fee5(HttpRunner):
    config = (
        Config("第二年Y2学费")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("第二年Y2学费")
                .post("/stdFee/pay.do")
                .with_headers(**{
                "Content - Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length": "246",
                "Host": "${ENV(Host)}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Cookie": "${ENV(COOKIE)}"
            })
                .with_data(
                            {
                            "_web_token": "$_web_token",
                            "learnId": "$learnId",
                            "grade": "$grade",
                            "years": "0",
                            "itemCodes": "Y2",
                            "accDeduction": "0.00",
                            "couponsStr": "[]",
                            "zmDeduction": "0",
                            "payableCount": "$feeAmount",
                            "paymentType": "1",
                            "remark": "",
                            "payData": '{"learnId":"$learnId","paymentType":"1","tradeType":"NATIVE","accDeduction":"0.00","zmDeduction":"0","coupons":"[]","items":"[{\\"orderNo\\":\\"$subOrderNo4\\",\\"itemCode\\":\\"Y1\\",\\"itemName\\":\\"代收第二年学费\\",\\"itemYear\\":\\"1\\",\\"amount\\":\\"$feeAmount\\",\\"accScale\\":0,\\"zmScale\\":0,\\"couponScale\\":0,\\"payAmount\\":\\"$feeAmount\\"}]","dataSources":"5","grade":"$grade","payAmount":"$feeAmount","remark":""}',
                                }
                            )

                .validate()
                .assert_equal("status_code", 200)
        )
]