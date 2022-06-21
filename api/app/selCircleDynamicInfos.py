from httprunner import HttpRunner, Config, Step, RunRequest
#获取圈子数据
class selCircleDynamicInfos(HttpRunner):
    config = (
        Config("获取圈子数据")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "scType": "1",                         #读书社:scType.2,  跑团：scType.3，  自考圈：scType.4	，同学圈：scType.1   ，职场圈：scType.5
                                            "grade": "2021研",
                                            "mobile": "$mobile",                    #登录手机号
                                            "pageSize": "$pageSize",
                                            # "userRoleType": "$userRoleType",       #账号身份
                                            "unvsId": "$unvsId",
                                            "pageNum": "$pageNum"
                                        },
                                    "header":{
                                            "appType": "3",

                                        }
                                },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("获取圈子数据")
                .post("/proxy/us/selCircleDynamicInfos/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                "Content-Type": "base64.b64encode",
                "Host": "${ENV(app_Host)}",
                "authtoken": "$app_auth_token",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0]", "body")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    selCircleDynamicInfos().test_start()