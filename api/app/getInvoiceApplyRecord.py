from httprunner import HttpRunner, Config, Step, RunRequest
#我的申请列表
class getInvoiceApplyRecord(HttpRunner):
    config = (
        Config("我的申请列表")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "android_version": "7.19.9",
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
            RunRequest("我的申请列表")
                .post("/proxy/bds/getInvoiceApplyRecord/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "frontTrace": "{\"transferSeq\":\"1\",\"phoneModel\":\"SM-N9500\",\"app_type\":\"android\",\"app_version\":\"7.19.9\",\"title\":\"myApplyType\",\"transferId\":\"165595504016790869\",\"uri\":\"/proxy/bds/myApplyType/1.0/\",\"phoneSys\":\"9\",\"app_sdk\":\"28\",\"sendTime\":\"1655955040168\"}",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].status", "$status")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    getInvoiceApplyRecord().test_start()