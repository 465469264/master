#商城购物提交订单
from httprunner import HttpRunner, Config, Step, RunRequest

class stuItemToPay(HttpRunner):
    config = (
        Config("商城购物提交订单")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                        "mappingId": "$mappingId",                           #由提交订单返回的支付id
                                        "exchangeCount": "$exchangeCount",                           #购买数量
                                        "accDeduction": "$accDeduction",                                #未知字段
                                        "zmScale": "$zmScale",                                      #商品的智米金额
                                        "payType": "WECHAT",                                 #支付方式
                                        "salesId": "$salesId",                             #商品id
                                        "payAmount": "$payAmount",                                 #总计应缴
                                        "zmDeduction": "$zmDeduction",                                 #优惠抵扣
                                        "payItem": "$payItem",                        #支付方式
                                        "saId": "$saId",
                                        "tradeType": "APP"
                                        },
                                    "header":{
                                        "appType":"3"
                                    }
                                },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("商城购物提交订单")
                .post("/proxy/us/stuItemToPay/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "frontTrace": "{\"transferSeq\":\"1\",\"phoneModel\":\"SM-N9500\",\"app_type\":\"android\",\"app_version\":\"7.19.9\",\"title\":\"getCertificateApply\",\"transferId\":\"165596882382164439\",\"uri\":\"/proxy/bds/getCertificateApply/1.0/\",\"phoneSys\":\"9\",\"app_sdk\":\"28\",\"sendTime\":\"1655968823822\"}",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "{ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    stuItemToPay().test_start()