from httprunner import HttpRunner, Config, Step, RunRequest

# 学员证明申请-----审核
class fdyCheck(HttpRunner):
    config = (
        Config("学员证明申请-----审核")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("学员证明申请-----审核")
                .post("/certificate/fdyCheck.do")
                .with_headers(**{
                "Accept":"*/*",
                "User-Agent":"PostmanRuntime/7.28.4",
                "Accept-Encoding":"gzip, deflate, br",
                "Connection":"keep-alive",
                "Cookie": "$Cookie",

    })
                .with_data({"certId": "$certId",
                            "learnId":"$learnId",
                            "applyTyp":"$applyTyp",    # 6>报读证明  5>其他,
                            "_web_token":"$_web_token",
                            "checkStatus":"checkStatus",        #-1>审核不通过      0>审核通过
                            "reason": "reason"                #审核备注

                            })
                .extract()
                .with_jmespath("body.body.data[0].certId","certId") #获取body
                .validate()
                .assert_equal("status_code", 200)
        )
    ]