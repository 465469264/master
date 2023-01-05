#2022-12-1，，，短视频版本增加的新接口，用于获取圈子的列表
from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from httprunner import HttpRunner, Config, Step, RunRequest
#获取签到返回
class getDictSettings(HttpRunner):
    config = (
        Config("用于获取圈子的列表")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "noCache": "1",
                                            "pId": "socialTab",
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
            RunRequest("用于获取圈子的列表")
                .post("/proxy/sys/getDictSettings/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "frontTrace": "{\"transferSeq\":\"1\",\"phoneModel\":\"SM-N9500\",\"app_type\":\"android\",\"app_version\":\"7.19.9\",\"title\":\"getCertificateApply\",\"transferId\":\"165596882382164439\",\"uri\":\"/proxy/bds/getCertificateApply/1.0/\",\"phoneSys\":\"9\",\"app_sdk\":\"28\",\"sendTime\":\"1655968823822\"}",
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
if __name__ == '__main__':
    getSignInfo().test_start()