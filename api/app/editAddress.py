from httprunner import HttpRunner, Config, Step, RunRequest
#购物添加收获地址
class eddit_address(HttpRunner):
    config = (
        Config("购物添加收获地址")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "saName": "测试",
                                            "address": "测试",
                                            "districtCode": "3633",
                                            "android_phoneModel": "SM-N9500",
                                            "districtName": "天河区",
                                            "cityCode": "1601",
                                            "provinceCode": "19",
                                            "mobile": "13729041111",
                                            "android_version": "7.19.2",
                                            "android_sdk": 28,
                                            "cityName": "广州市",
                                            "saType": "3",
                                            "CREATOR": {},
                                            "provinceName": "广东",
                                            "excType": "1",
                                            "email": "12@qq.com"
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
            RunRequest("购物添加收获地址")
                .post("/proxy/us/editAddress/1.0/")
                .with_headers(**{
                "Accept - Encoding": "gzip",
                "User-Agent": "Android/environment=test/app_version=7.19.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "$app_auth_token",
                            })
                .with_data('$data')
                .validate()
                .assert_equal("status_code", 200)
        )
    ]