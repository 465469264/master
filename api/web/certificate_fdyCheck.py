from httprunner import HttpRunner, Config, Step, RunRequest

# 学员证明申请-----审核
class fdyCheck(HttpRunner):
    config = (
        Config("学员证明申请-----审核")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables(**({"url":"${ENV(BASE_URL)}"})

        )
    )
    teststeps = [
        Step(
            RunRequest("学员证明申请-----审核")
                .post("/certificate/fdyCheck.do")
                .with_headers(**{
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'transferSeq': '1',
                'X-Requested-With': 'XMLHttpRequest',
                "Host": "${ENV(Host)}",
                "Cookie": "$Cookie",
                })
                # checkStatus  -1>审核不通过      0>审核通过             "applyTyp":"$applyTyp",    # 6>报读证明  5>其他,    "reason": "$reason",                #审核备注
                .with_data({'certId': '$certId', 'learnId': '$learnId', 'applyType': '$applyType', '_web_token': '', 'ifSubmit': '', 'checkStatus': '$checkStatus', 'reason': '$reason', 'admin-role-save': ''})
                .extract()
                .validate()
                .assert_equal("body.code", "00")
        )
    ]