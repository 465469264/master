from httprunner import HttpRunner, Config, Step, RunRequest
#获取可申请发票订单
class getInvoiceApply(HttpRunner):
    config = (
        Config("获取可申请发票订单")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "learnId": "$learnId",
                                            "android_version": "7.19.1",
                                            "android_phoneModel": "SM-N9500",
                                            "android_sdk": 28
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
            RunRequest("获取可申请发票订单")
                .post("/proxy/bds/getInvoiceApply/1.0/")
                .with_headers(**{
                "Accept - Encoding": "gzip",
                "User-Agent": "Android/environment=test/app_version=7.19.1/sdk=30/dev=Xiaomi/phone=Mi 10/android_system=11",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                # "Host": "test.yzwill.cn",
                "authtoken": "$app_auth_token",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[1].bdSubOrderId", "bdSubOrderId")
                .with_jmespath("body.body[1].itemCode", "itemCode")
                .with_jmespath("body.body[1].itemName", "itemName")
                .with_jmespath("body.body[1].grade", "grade")
                .with_jmespath("body.body[1].payment", "payment")
                .with_jmespath("body.body[1].invoiceType", "invoiceType")

                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    getInvoiceApply().test_start()