from httprunner import HttpRunner, Config, Step, RunRequest

# 学员证明申请列表
class certificate_findAllList(HttpRunner):
    config = (
        Config("学员证明申请列表")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("学员证明申请列表")
                .post("/certificate/findAllList.do")
                .with_headers(**{
                "Accept":"*/*",
                "User-Agent":"PostmanRuntime/7.28.4",
                "Accept-Encoding":"gzip, deflate, br",
                "Connection":"keep-alive",
                "Cookie": "$Cookie",

    })
                .with_data({"start": "$start",
                            "length":"$length",
                            "stdName":"$stdName"   #学员姓名
                            })
                .extract()
                .with_jmespath("body.body.data[0].certId","certId")
                .with_jmespath("body.body.data[0].applyType", "applyType")

                .validate()
                .assert_equal("status_code", 200)
        )
    ]