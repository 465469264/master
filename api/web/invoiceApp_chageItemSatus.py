from httprunner import HttpRunner, Config, Step, RunRequest
#更改发票状态
class invoiceApp_chageItemSatus(HttpRunner):
    config = (
        Config("更改发票状态")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("更改发票状态")
                .post("/invoiceApp/chageItemSatus.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"$Cookie"

    })
                .with_data({"itemId": "$itemId",
                            "learnId": "$learnId",
                            "itemName": "$itemName",
                            "status": "$status"                     #1>审核通过       2>驳回
                            })
                .extract()
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    invoiceApp_chageItemSatus().test_start()