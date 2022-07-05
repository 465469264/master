from httprunner import HttpRunner, Config, Step, RunRequest
#查询发票申请列表
class invoiceApp_itemList(HttpRunner):
    config = (
        Config("查询发票申请列表")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("查询发票申请列表")
                .post("/invoiceApp/itemList.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"$Cookie"

    })
                .with_data({"mobile": "$mobile"})
                .extract()
                .with_jmespath("body.body.data[0].itemId", "itemId")
                .with_jmespath("body.body.data[0].itemName", "itemName")
                .with_jmespath("body.body.data[0].learnId", "learnId")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    invoiceApp_itemList().test_start()