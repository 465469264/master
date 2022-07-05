from httprunner import HttpRunner, Config, Step, RunRequest
#我的优惠券
class myCoupons(HttpRunner):
    config = (
        Config("我的优惠券")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                         "recruitType": "$recruitType",                 #查所有时不需要传  ，查对应优惠政策优惠券时传1
                                        "scholarship": "$scholarship"                   #优惠情况，前端会调两次接口，一次查询有优惠政策对应的优惠券，第二次查询所有，测试数据优惠政策：1273
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
            RunRequest("我的优惠券")
                .post("/proxy/bds/myCoupons/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "frontTrace": "{\"transferSeq\":\"1\",\"phoneModel\":\"SM-N9500\",\"app_type\":\"android\",\"app_version\":\"7.19.9\",\"title\":\"getCertificateApply\",\"transferId\":\"165596882382164439\",\"uri\":\"/proxy/bds/getCertificateApply/1.0/\",\"phoneSys\":\"9\",\"app_sdk\":\"28\",\"sendTime\":\"1655968823822\"}",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    myCoupons().test_start()