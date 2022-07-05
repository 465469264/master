from httprunner import HttpRunner, Config, Step, RunRequest
#获取我的地址
class myAddress(HttpRunner):
    config = (
        Config("获取我的地址")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                        "saType": "$saType",              #地址类型	  1>教材地址	  2>试卷邮寄地址	  3>收货物地址
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
            RunRequest("获取我的地址")
                .post("/proxy/us/myAddress/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "frontTrace": "{\"transferSeq\":\"1\",\"phoneModel\":\"SM-N9500\",\"app_type\":\"android\",\"app_version\":\"7.19.9\",\"title\":\"getCertificateApply\",\"transferId\":\"165596882382164439\",\"uri\":\"/proxy/bds/getCertificateApply/1.0/\",\"phoneSys\":\"9\",\"app_sdk\":\"28\",\"sendTime\":\"1655968823822\"}",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].saId", "saId")
                .with_jmespath("body.body[0].districtCode", "districtCode")    #区
                .with_jmespath("body.body[0].districtName", "districtName")
                .with_jmespath("body.body[0].provinceCode", "provinceCode")    #省
                .with_jmespath("body.body[0].provinceName", "provinceName")
                .with_jmespath("body.body[0].cityName", "cityName")          #市
                .with_jmespath("body.body[0].cityCode", "cityCode")
                .with_jmespath("body.body[0].streetName", "streetName")      #县
                .with_jmespath("body.body[0].streetCode", "streetCode")
                .with_jmespath("body.body[0].address", "address")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    myAddress().test_start()