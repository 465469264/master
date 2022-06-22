from httprunner import HttpRunner, Config, Step, RunRequest
#获取需要完善的资料
class getInvoiceApply(HttpRunner):
    config = (
        Config("获取需要完善的资料")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "learnId": "$learnId",
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
            RunRequest("获取需要完善的资料")
                .post("/proxy/bds/getNeedCompleteStuInfo/1.0/")
                .with_headers(**{
                "Accept - Encoding": "gzip",
                "User-Agent": "Android/environment=test/app_version=7.19.1/sdk=30/dev=Xiaomi/phone=Mi 10/android_system=11",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "$app_auth_token",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.idCard", "idCard")
                .with_jmespath("body.body.stdId", "stdId")
                .with_jmespath("body.body.annexList[0].annexId", "annexId0")
                .with_jmespath("body.body.annexList[0].annexType", "annexType0")
                .with_jmespath("body.body.annexList[0].annexName", "annexName0")
                .with_jmespath("body.body.annexList[1].annexId", "annexId1")
                .with_jmespath("body.body.annexList[1].annexType", "annexType1")
                .with_jmespath("body.body.annexList[1].annexName", "annexName1")
                .with_jmespath("body.body.annexList[2].annexId", "annexId2")
                .with_jmespath("body.body.annexList[2].annexType", "annexType2")
                .with_jmespath("body.body.annexList[2].annexName", "annexName2")
                .with_jmespath("body.body.annexList[3].annexId", "annexId3")
                .with_jmespath("body.body.annexList[3].annexType", "annexType3")
                .with_jmespath("body.body.annexList[3].annexName", "annexName3")
                .with_jmespath("body.body.annexList[4].annexId", "annexId4")
                .with_jmespath("body.body.annexList[4].annexType", "annexType4")
                .with_jmespath("body.body.annexList[4].annexName", "annexName4")
                .with_jmespath("body.body.annexList[5].annexId", "annexId5")
                .with_jmespath("body.body.annexList[5].annexType", "annexType5")
                .with_jmespath("body.body.annexList[5].annexName", "annexName5")
                .with_jmespath("body.body.birthday", "birthday")
                .with_jmespath("body.body.stdName", "stdName")
                .with_jmespath("body.body.jobType", "jobType")
                .with_jmespath("body.body.sex", "sex")
                .with_jmespath("body.body.isOpenUnvs", "isOpenUnvs")
                .with_jmespath("body.body.isDataCheck", "isDataCheck")
                .with_jmespath("body.body.politicalStatus", "politicalStatus")
                .with_jmespath("body.body.recruitType", "recruitType")
                .with_jmespath("body.body.annexStatus", "annexStatus")

                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    getInvoiceApply().test_start()