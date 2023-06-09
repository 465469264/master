#获取版本信息
from httprunner import HttpRunner, Config, Step, RunRequest

class getAPPVersionInfo(HttpRunner):
    config = (
        Config("获取版本信息")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                        "android_phoneModel": "SM-N9500",
                                        "appType": "android",
                                        "model": "SM-N9500",
                                        "deviceVersion": "9",
                                        "facturer": "samsung",
                                        "android_version": "7.19.13.2",
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
            RunRequest("获取版本信息")
                .post("/proxy/bds/getAPPVersionInfo/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "frontTrace": "{\"transferSeq\":\"1\",\"phoneModel\":\"SM-N9500\",\"app_type\":\"android\",\"app_version\":\"7.19.9\",\"title\":\"getCertificateApply\",\"transferId\":\"165596882382164439\",\"uri\":\"/proxy/bds/getCertificateApply/1.0/\",\"phoneSys\":\"9\",\"app_sdk\":\"28\",\"sendTime\":\"1655968823822\"}",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                            })
                .with_data('$data')
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    getAPPVersionInfo().test_start()