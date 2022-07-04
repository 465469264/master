from httprunner import HttpRunner, Config, Step, RunRequest
#智米商城-返回京东商品
class goodsList(HttpRunner):
    config = (
        Config("商品列表")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                        "salesType": "$salesType",         #1>兑换活动  2>抽奖活动  3>竞价活动  4>生日活动
                                        "pageSize": "$pageSize",
                                        "pageNum": "$pageNum",
                                        "goodsType": "$goodsType"           #1>普通商品	 2>课程商品	3>活动商品	4>教材商品	 5>生日商品
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
            RunRequest("商品列表")
                .post("/proxy/gs/goodsList/1.0/")
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
    goodsList().test_start()