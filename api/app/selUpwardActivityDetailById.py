#获取活动详情
from httprunner import HttpRunner, Config, Step, RunRequest
class selUpwardActivityDetailById(HttpRunner):
    config = (
        Config("获取活动详情")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                     "actId": "$actId"
                                    },
                                    "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("获取活动详情")
                .post("/proxy/mkt/selUpwardActivityDetailById/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "authtoken": "${ENV(app_auth_token)}",
                            "Host": "${ENV(app_Host)}"
                }
            )
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.actName", "actName")       #活动名称
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.body.actName", "$actName")  # 活动名称

        )
    ]





if __name__ == '__main__':
    selUpwardActivityDetailById().test_start()
