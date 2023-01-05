#首页不知道什么接口---接口文档找不到
from httprunner import HttpRunner, Config, Step, RunRequest

class selAppPostingInfos(HttpRunner):
    config = (
        Config("首页不知道什么接口---接口文档找不到")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                        "pageSize": "$pageNum",
                                        "pageNum": "$pageNum"
                                        },
                                    "header":{
                                        "appType":"4"
                                    }
                                },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("首页不知道什么接口---接口文档找不到")
                .post("/proxy/us/selAppPostingInfos/1.0/")
                .with_headers(**{
                "User-Agent": "yuan zhi jiao yu/7.19.8 (iPhone; iOS 15.0.2; Scale/3.00)",
                "frontTrace": "{\"transferSeq\":\"1\",\"phoneModel\":\"SM-N9500\",\"app_type\":\"android\",\"app_version\":\"7.19.9\",\"title\":\"getCertificateApply\",\"transferId\":\"165596882382164439\",\"uri\":\"/proxy/bds/getCertificateApply/1.0/\",\"phoneSys\":\"9\",\"app_sdk\":\"28\",\"sendTime\":\"1655968823822\"}",
                "Content-Type": "text/yzedu+",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    scholarshipStoryList().test_start()