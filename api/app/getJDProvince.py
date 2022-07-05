from httprunner import HttpRunner, Config, Step, RunRequest
#获取省份
class GetJDProvince(HttpRunner):
    config = (
        Config("获取省份")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
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
            RunRequest("获取省份")
                .post("/proxy/gs/getJDProvince/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "frontTrace": "{\"transferSeq\":\"1\",\"phoneModel\":\"SM-N9500\",\"app_type\":\"android\",\"app_version\":\"7.19.9\",\"title\":\"getCertificateApply\",\"transferId\":\"165596882382164439\",\"uri\":\"/proxy/bds/getCertificateApply/1.0/\",\"phoneSys\":\"9\",\"app_sdk\":\"28\",\"sendTime\":\"1655968823822\"}",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[13].name", "provinceName")
                .with_jmespath("body.body[13].code", "provinceCode")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    GetJDProvince().test_start()