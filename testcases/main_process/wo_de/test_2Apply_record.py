from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.getInvoiceApply import getInvoiceApply
from api.app.studentInvoiceApply import ApplyRecord
from api.app.loginOrRegister import app_login
from api.app.stdLearnInfo import stdLearnInfo
from api.web.invoiceApp_itemList import invoiceApp_itemList
from api.web.invoiceApp_chageItemSatus import invoiceApp_chageItemSatus
from api.app.getInvoiceApplyRecord import getInvoiceApplyRecord
from api.app.myApplyType import myApplyType
from api.app.getInvoiceApplyRecord import getInvoiceApplyRecord

class Test_Apply_Record(HttpRunner):
    config = (
        Config("申请模块")
            .verify(False)
            .variables(**{
                "mobile": "${read_data_number(ApplyRecord,mobile)}"
                })
    )
    teststeps = [
        Step(RunTestCase("登录申请发票的手机号").call(app_login).export(*["app_auth_token","userId"])),
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("获取可申请的类型").call(myApplyType)),
        Step(RunTestCase("获取可申请发票订单").call(getInvoiceApply).export(*["bdSubOrderId", "itemCode","learnId","itemName", "grade", "payment","invoiceType"])),
        Step(RunTestCase("申请企业发票").with_variables(**({"companyTaxNumber" :"123456789111111111","invoiceTitle": "1","companyName": "测试","applyPurpose": "测试","email": "123@qq.com"})).call(ApplyRecord)),
        Step(RunTestCase("号码搜索发票列表").setup_hook('${login_web()}', "Cookie").call(invoiceApp_itemList).export(*["itemId", "itemName","Cookie"])),
        Step(RunTestCase("驳回发票申请").with_variables(**({"status":"2"})).call(invoiceApp_chageItemSatus)),
        Step(RunTestCase("获取申请列表的发票申请第一条是审核不通过").with_variables(**({"status":"2"})).call(getInvoiceApplyRecord)),

        #异常传参
        Step(RunTestCase("申请企业发票,不传发票号").with_variables(**({"companyTaxNumber": "", "invoiceTitle": "1", "companyName": "测试", "applyPurpose": "测试","email": "123@qq.com"})).call(ApplyRecord)),
        Step(RunTestCase("驳回发票申请").with_variables(**({"status": "2"})).call(invoiceApp_chageItemSatus)),
        Step(RunTestCase("申请企业发票,不传邮箱").with_variables(**({"companyTaxNumber": "", "invoiceTitle": "1", "companyName": "测试", "applyPurpose": "测试","email": ""})).call(ApplyRecord)),
        Step(RunTestCase("驳回发票申请").with_variables(**({"status": "2"})).call(invoiceApp_chageItemSatus)),
        Step(RunTestCase("申请个人发票,传邮箱及企业名称").with_variables(**({"companyTaxNumber" :"123456789111111111","invoiceTitle": "2","companyName": "测试","applyPurpose": "测试","email": "123@qq.com"})).call(ApplyRecord)),
        Step(RunTestCase("驳回发票申请").with_variables(**({"status": "2"})).call(invoiceApp_chageItemSatus)),

    ]

if __name__ == '__main__':
    Test_Apply_Record().test_start()