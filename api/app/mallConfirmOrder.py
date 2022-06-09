from httprunner import HttpRunner, Config, Step, RunRequest
#购物纯智米商品
class buy_goods(HttpRunner):
    config = (
        Config("购买商城商品")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "exchangeCount": "1",
                                            "payType": "WECHAT",
                                            "salesId": "163825496915753631",
                                            "android_phoneModel": "SM-N9500",
                                            "android_version": "7.19.2",
                                            "saId": "66450",
                                            "android_sdk": 28
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
            RunRequest("购买商城商品")
                .post("/proxy/gs/mallConfirmOrder/1.0/")
                .with_headers(**{
                "Accept - Encoding": "gzip",
                "User-Agent": "Android/environment=test/app_version=7.19.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "{ENV(app_Host)}",
                "authtoken": "$app_auth_token",
                            })
                .with_data('$data')
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    buy_goods().test_start()