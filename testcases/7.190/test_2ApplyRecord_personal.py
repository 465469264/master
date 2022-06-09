from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.getInvoiceApply import getInvoiceApply
from api.app.studentInvoiceApply import ApplyRecord
from api.app.loginOrRegister import app_login
from api.app.stdLearnInfo import stdLearnInfo

class TestCases_ApplyRecord_personal(HttpRunner):
    config = (
        Config("申个人发票用例")
            .verify(False)
            .variables(**{
                "mobile": "${read_data_number(ApplyRecord,mobile)}"
                })
    )
    teststeps = [
        # 缴费辅导费,并生成学院订单
        Step(RunTestCase("登录申请发票的手机号").call(app_login).export(*["app_auth_token","userId"])),
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("获取可申请发票订单").call(getInvoiceApply).export(*["bdSubOrderId", "itemCode","learnId","itemName", "grade", "payment","invoiceType"])),
        Step(RunTestCase("申请个人发票").with_variables(**({"companyTaxNumber" :"","invoiceTitle": "2","companyName": "",
                                                      "applyPurpose": "测试","email": "123@qq.com"})).call(ApplyRecord)),
    ]

if __name__ == '__main__':
    TestCases_ApplyRecord_personal().test_start()