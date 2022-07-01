from httprunner import HttpRunner, Config, Step, RunRequest
#添加/修改商品
class goodsUpdate(HttpRunner):
    config = (
        Config("添加/修改商品")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("添加/修改商品")
                .post("/goods/goodsUpdate.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"$Cookie"

    })
                .with_data({"exType": "Add",                         #Add>添加
                            "goodsType": "1",                       #1>自营商品
                            "goodsName": "自动添加1",
                            "goodsCount": "100",                    #库存
                            "costPrice": "1000",                    #1>成本价
                            "originalPrice":"1000",              #显示市场价
                            "isAllow": "1",                      #1>启用
                            "annexUrl":"gs/165665654126285008/80745D3151034ADE9A2754CFAA29EDEF.jpg",                       #上坪封面
                            "isPhotoChange": "1",                #未知字段
                            "goodsDesc": "自动添加1",            #简介
                            "goodsContent":"<p>自动添加1</p>"    #详细介绍

                            }
                            )
                .extract()
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    goodsUpdate().test_start()