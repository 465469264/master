from httprunner import HttpRunner, Config, Step, RunRequest
#智米攻略
class zmRaiders(HttpRunner):
    config = (
        Config("智米攻略")
            .base_url("http://27-app.yzwill.cn")
            .verify(False)
            .variables(**{})
        )
    teststeps = [
        Step(
            RunRequest("智米攻略")
                .get("/zmRaiders")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Host": "27-app.yzwill.cn",
                            "Accept-Encoding": "gzip, deflate",
                            "Accept-Language":"zh-CN,zh-Hans;q=0.9",
                            "authtoken": "authToken=LiCnP2Q57t9k/8YUl6PJ9V6MincFQEXxoQPgdqPPNCvNHISelVxSH9Gt5g2A7Rwr",

                }
            )
                # .with_data('$data')
                .extract()
                .with_jmespath("body", "body")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    zmRaiders().test_start()




if __name__ == '__main__':
    zmRaiders().test_start()
