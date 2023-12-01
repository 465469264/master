#app端扫二维码登录学员系统
from httprunner import HttpRunner, Config, Step, RunRequest
class login_code(HttpRunner):
    config = (
        Config("获取APP登录得二维码sessionId")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                "body": {
                                    "source": "1",
                                    "userId": "$userId",
                                    "callbackUrl": "https://new.yzou.cn/scanCodeCallBack.do",
                                    "sessionId": "$sessionId",
                                    "flag": "$flag",            #1：扫码确认   2：确认登录
                                },
                                "header": {
                                    "appType": "3",
                                }
                            },
                            "data": "${base64_encode($number)}"
                            },
                            )
            )
    teststeps = [
        Step(
            RunRequest("APP扫学员系统二维码")
                .post("/proxy/us/loginByQrCode/1.0/")
                .with_headers(**{
                            "User-Agent": "yuan zhi jiao yu/7.26.6 (iPhone; iOS 16.6.1; Scale/3.00)",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "${ENV(app_auth_token)}",
    }
            )
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message","$message")
        )
    ]
