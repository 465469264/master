from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.getInvoiceApply import getInvoiceApply
from api.app.studentInvoiceApply import ApplyRecord
from api.app.loginOrRegister import app_login
from api.app.stdLearnInfo import stdLearnInfo
from api.web.invoiceApp_itemList import invoiceApp_itemList
from api.web.invoiceApp_chageItemSatus import invoiceApp_chageItemSatus
from api.app.userHome import get_info

class TestCases_ApplyRecord_enterprise(HttpRunner):
    config = (
        Config("申请企业发票用例")
            .verify(False)
            .variables(**{
                "mobile": "${read_data_number(ApplyRecord,mobile)}",
                "message": "success",
                "body": "SUCCESS",
                })
    )
    teststeps = [
        Step(RunTestCase("获取信息").call(get_info).teardown_hook('${login_web()}', "Cookie").export(*["userId","Cookie"])),
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("获取可申请发票订单").call(getInvoiceApply).export(*["bdSubOrderId", "itemCode","learnId","itemName", "grade", "payment","invoiceType"])),
        Step(RunTestCase("申请企业发票").with_variables(**({"companyTaxNumber" :"123456789111111111","invoiceTitle": "1","companyName": "测试",
                                                    "applyPurpose": "测试","email": "123@qq.com"})).call(ApplyRecord)),
        Step(RunTestCase("号码搜索发票列表").call(invoiceApp_itemList).export(*["itemId", "itemName"])),
        Step(RunTestCase("驳回发票申请").with_variables(**({"status":"2"})).call(invoiceApp_chageItemSatus)),
    ]

if __name__ == '__main__':
    TestCases_ApplyRecord_enterprise().test_start()