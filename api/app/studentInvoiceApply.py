from httprunner import HttpRunner, Config, Step, RunRequest
#申请发票
class ApplyRecord(HttpRunner):
    config = (
        Config("申请发票")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                            "learnId": "$learnId",
                                            "companyTaxNumber": "$companyTaxNumber",
                                            "invoiceTitle": "$invoiceTitle",           #抬头类型  1->企业, 2->个人
                                            "userId": "$userId",
                                            "bdsInvoiceItem": "[{\"amount\":\"$payment\",\"itemName\":\"$itemName\",\"invoiceType\":$invoiceType,\"subOrderNo\":\"$bdSubOrderId\",\"expressFee\":\"15\",\"itemCode\":\"$itemCode\"}]",
                                            "companyName": "$companyName",
                                            "hasPaperInvoice": 0,
                                            "email": "$email",
                                            "applyPurpose": "$applyPurpose",
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
            RunRequest("申请发票")
                .post("/proxy/bds/studentInvoiceApply/1.0/")
                .with_headers(**{
                                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                                "frontTrace": "{\"transferSeq\":\"1\",\"phoneModel\":\"SM-N9500\",\"app_type\":\"android\",\"app_version\":\"7.19.9\",\"title\":\"getCertificateApply\",\"transferId\":\"165596882382164439\",\"uri\":\"/proxy/bds/getCertificateApply/1.0/\",\"phoneSys\":\"9\",\"app_sdk\":\"28\",\"sendTime\":\"1655968823822\"}",
                                "Content-Type": "text/yzedu+; charset=UTF-8",
                                "Host": "${ENV(app_Host)}",
                                "authtoken":"${ENV(app_auth_token)}",
                                })

                .with_data('$data')
                .validate()
                .assert_equal("body.message", "$message")

        )
    ]