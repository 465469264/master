from httprunner import HttpRunner, Config, Step, RunRequest
#获取上传图片的token信息
class getStsToken(HttpRunner):
    config = (
        Config("获取上传图片的token信息")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "timeStamp": "${timestap()}",
                                            },
                                    "header": {"appType": "${ENV(appType)}"}
                                        },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("获取上传图片的token信息")
                .post("/proxy/proxy/getStsToken/1.0/")
                .with_headers(**{
                                "User-Agent": "${ENV(User-Agent)}",
                                "Content-Type": "text/yzedu+; charset=UTF-8",
                                "Host": "${ENV(app_Host)}",
                                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.accessKeyId", "accessKeyId")
                .with_jmespath("body.body.accessKeySecret", "accessKeySecret")
                .with_jmespath("body.body.endpoint", "endpoint")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    getStsToken().test_start()
