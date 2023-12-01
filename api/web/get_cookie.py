#与服务器建立连接，获取到cookie
from httprunner import HttpRunner, Config, Step, RunRequest
class get_cookie(HttpRunner):
    config = (
        Config("与服务器建立连接，拼接cookie")
            .base_url("${ENV(web_url)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("与服务器建立连接，拼接cookie")
                .get("/toLogin.do")
                .extract()
                .with_jmespath("headers","headers")
                .validate()
        )
    ]
if __name__ == '__main__':
    get_cookie().test_start()