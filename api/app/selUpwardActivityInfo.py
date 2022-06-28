from httprunner import HttpRunner, Config, Step, RunRequest
#获取圈子页的活动
class selUpwardActivityInfo(HttpRunner):
    config = (
        Config("获取圈子页的活动")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                    "sign": "86E4295F988D9CDADB9CBB4494B71692",
                                    },
                                    "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("获取圈子页的活动")
                .post("/proxy/mkt/selUpwardActivityInfo/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "authtoken": "${ENV(app_auth_token)}",
                            "Host": "${ENV(app_Host)}"
                }
            )
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].id", "id")                #活动id
                .with_jmespath("body.body[0].actName", "actName")       #活动名称
                .validate()
                .assert_equal("status_code", 200)
        )
    ]





if __name__ == '__main__':
    selUpwardActivityInfo().test_start()
