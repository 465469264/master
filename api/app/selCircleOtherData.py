#圈子页-我的读书笔记
from httprunner import HttpRunner, Config, Step, RunRequest
class selCircleVideoInfo(HttpRunner):
    config = (
        Config("圈子页-我的读书笔记")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "cirLocationData": [
                                                                {
                                                                    "mappingId": "1614",
                                                                    "subType": 1,
                                                                    "scType": "2",
                                                                    "ifGisData": "0"
                                                                }
                                                            ]
                                        },
                                    "header":{
                                            "appType": "3",
                                        }
                                },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("圈子页-我的读书笔记")
                .post("/proxy/us/selCircleOtherData/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",

                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]