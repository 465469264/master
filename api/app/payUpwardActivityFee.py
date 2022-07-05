from httprunner import HttpRunner, Config, Step, RunRequest
#付款活动报名
class payUpwardActivityFee(HttpRunner):
    config = (
        Config("付款活动报名")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                        "amount": "$amount",
                                        "payType": "$payType",                #支付类型：17
                                        "tradeType": "$tradeType",                   #付费方，APP,H5等
                                        "zmDeduction": "$zmDeduction",                 #智米抵扣
                                        "orderNo": "$orderNo",                #活动付费订单id
                                        "accDeduction": "$accDeduction",              #实际付款
                                        "actId": "$actId"                         #活动id
                                        },
                                        "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("付款活动报名")
                .post("/proxy/bds/payUpwardActivityFee/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "${ENV(app_auth_token)}",
            }
            )
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")


        )
    ]
if __name__ == '__main__':
   payUpwardActivityFee().test_start()


