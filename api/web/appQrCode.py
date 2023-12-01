#学员系统>获取APP登录得二维码sessionId
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class app_QrCode(HttpRunner):
    config = (
        Config("获取APP登录得二维码sessionId")
            .base_url("${ENV(web_url)}")
            .verify(False)
            .variables(**{})
        )
    teststeps = [
        Step(
            RunRequest("获取APP登录得二维码sessionId")
                .get("/appQrCode.do")
                .with_headers(**{
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                }
            )
                .extract()
                .with_jmespath("body.body.sessionId", "sessionId")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    app_QrCode().test_start()