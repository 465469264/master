from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.getInvoiceApply import getInvoiceApply
from api.app.studentInvoiceApply import ApplyRecord
from api.web.stdFee_listdo import querry
from api.web.college_stdFee_listdo import querry2
from api.web.stdFee_toPay import web_token
from api.web.stdFee_pay_do import pay_fee
from api.web.stdFee_pay_S1_do import pay_fee2
from api.web.stdFee_pay_Y1_do import pay_fee3
from api.web.feeReview_list_do import feeReview_list
from api.web.feeReview_reviewFees_do import reviewFee1
from api.web.login_web_test import login
from api.app.loginOrRegister import app_login

class TestCasesPay_fee(HttpRunner):
    config = (
        Config("申请发票用例")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables(**{
                "mobile": "${read_data_number(test_data,register_mobile_chengjiao)}"
                })
    )
    teststeps = [
        # 缴费辅导费,并生成学院订单
        Step(RunTestCase("获取缴费信息,并生成学院订单").call(querry).teardown_hook('${College_order($learn_Id)}').export(*["learnId","learn_Id","subOrderNo","grade","feeAmount"])),
        Step(RunTestCase("获取缴费web_token").call(web_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("缴辅导费").call(pay_fee)),
        # 删除没用的学院订单,缴费学院订单
        Step(RunTestCase("获取缴费信息,删除没用的学院订单").call(querry2).teardown_hook('${delete_order($learn_Id)}').export(*["subOrderNo1","subOrderNo2","subOrderNo3","subOrderNo4","subOrderNo5","subOrderNo6","grade","feeAmount"])),
        Step(RunTestCase("获取学院订单缴费web_token").call(web_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("缴第一年S1").call(pay_fee2)),
        Step(RunTestCase("获取学院订单缴费web_token").call(web_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("缴第一年Y1").call(pay_fee3)),
        Step(RunTestCase("查找缴费审核学员").call(feeReview_list).export(*["subOrderNo1", "subOrderNo2","subOrderNo3"])),
        Step(RunTestCase("批量审核").call(reviewFee1).teardown_hook('${std_stage($learn_Id)}')),   #批量审核后，让学员变为在线学员
        Step(RunTestCase("登录刚注册的手机号").call(app_login).export(*["app_auth_token","userId"])),
        Step(RunTestCase("获取可申请发票订单").call(getInvoiceApply).export(*["bdSubOrderId", "itemCode", "itemName", "grade", "payment","invoiceType"])),
        Step(RunTestCase("申请发票").call(ApplyRecord)),
    ]

if __name__ == '__main__':
    a = login().login()
    TestCasesPay_fee().test_start()