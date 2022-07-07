from httprunner import HttpRunner, Config, Step, RunRequest
#首页礼品商城热门推荐
class selAppGoodsShop(HttpRunner):
    config = (
        Config("首页礼品商城热门推荐")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": { "header": {
                                        "appType": "4",
                                    },
                                    "body": {
                                        "salesType": "$salesType",                   #1>兑换活动  2>抽奖活动  3>竞价活动  4>生日活动
                                        "pageSize": "$pageSize",                    #1>显示一个，2>显示两个
                                        "pageNum": "$pageNum",                     #页码
                                        "goodsType": "$goodsType"                   #1>普通商品	 2>课程商品	3>活动商品	4>教材商品	 5>生日商品
                                    }
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("首页礼品商城热门推荐")
                .post("/proxy/us/selAppGoodsShop/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].goodName","goodName")
                .validate()
                .assert_equal("body.message", "$message")

        )
    ]

if __name__ == '__main__':
    selAppGoodsShop().test_start()