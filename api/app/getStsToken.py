from httprunner import HttpRunner, Config, Step, RunRequest
#获取上传图片的token信息
class getStsToken(HttpRunner):
    config = (
        Config("获取上传图片的token信息")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{

                                            "sign": "A4B51C6799BB72CFA56151F6D5F2FAC6",
                                            "iOS_version": "7.19.4",
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
            RunRequest("获取上传图片的token信息")
                .post("/proxy/proxy/getStsToken/1.0/")
                .with_headers(**{
                'traceSeq': '1',
                'User-Agent': 'Android/environment=test/app_version=7.12.3/sdk=28/dev=xiaomi/phone=Redmi 6/android_system=9',
                'frontTrace': '{"transferSeq":"1","phoneModel":"Redmi 6","app_type":"android","app_version":"7.12.3","title":"%E8%8E%B7%E5%BE%97oss%E4%B8%8A%E4%BC%A0token","transferId":"163296339421021756","uri":"/proxy/proxy/getStsToken/1.0/","phoneSys":"9","app_sdk":"28","sendTime":"1632963394223"}',
                'Content-Type': 'text/yzedu+; charset=UTF-8',
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.accessKeyId", "accessKeyId")
                .with_jmespath("body.body.accessKeySecret", "accessKeySecret")
                .with_jmespath("body.body.endpoint", "endpoint")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    getStsToken().test_start()
