from httprunner import HttpRunner, Config, Step, RunRequest
#登录学员系统端
class login_web(HttpRunner):
    config = (
        Config("登录学员系统端")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("登录web端")
                .post("/loginByMobile.do")
                .with_headers(**{
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "uri": "http://bms.yzwill.cn/toLogin.do",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            })
                .with_data({"isOpenImage": "",
                            "mobile": "18221823862",
                            "ImgValidCode": "",
                            "validCode": "888888"
                             })
                .extract()
                .with_jmespath("cookies.SESSION", "cookies")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    login_web().test_start()