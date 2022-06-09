from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.getInvoiceApply import getInvoiceApply
from api.app.studentInvoiceApply import ApplyRecord
from api.app.loginOrRegister import app_login
from api.app.stdLearnInfo import stdLearnInfo

class TestCases_ApplyRecord_enterprise(HttpRunner):
    config = (
        Config("申请企业发票用例")
            .verify(False)
            .variables(**{
                "mobile": "${read_data_number(ApplyRecord,mobile)}"
                })
    )
    teststeps = [
        Step(RunTestCase("登录申请发票的手机号").call(app_login).export(*["app_auth_token","userId"])),
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("获取可申请发票订单").call(getInvoiceApply).export(*["bdSubOrderId", "itemCode","learnId","itemName", "grade", "payment","invoiceType"])),
        Step(RunTestCase("申请企业发票").with_variables(**({"companyTaxNumber" :"123456789111111111","invoiceTitle": "1","companyName": "测试",
                                                      "applyPurpose": "测试","email": "123@qq.com"})).call(ApplyRecord)),
    ]

if __name__ == '__main__':
    TestCases_ApplyRecord_enterprise().test_start()