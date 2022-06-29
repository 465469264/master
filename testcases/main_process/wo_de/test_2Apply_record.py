import pytest,sys,os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
print(str(Path(__file__).parent.parent.parent.parent))

from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.getInvoiceApply import getInvoiceApply
from api.app.studentInvoiceApply import ApplyRecord
from api.app.stdLearnInfo import stdLearnInfo
from api.web.invoiceApp_itemList import invoiceApp_itemList
from api.web.invoiceApp_chageItemSatus import invoiceApp_chageItemSatus
from api.app.myApplyType import myApplyType
from api.app.getInvoiceApplyRecord import getInvoiceApplyRecord
from api.app.userHome import get_info

class TestApply_Record(HttpRunner):
    @pytest.mark.parametrize("param",Parameters({"companyTaxNumber-invoiceTitle-companyName-applyPurpose-email":"${Apply_record()}"}))
    def test_start(self,param):
        super().test_start(param)
    config = (
        Config("申请模块")
            .verify(False)
            .variables(**{
                "mobile": "${read_data_number(ApplyRecord,mobile)}"
                })
    )
    teststeps = [
        Step(RunTestCase("获取信息").call(get_info).export(*["userId"])),
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("获取可申请的类型").call(myApplyType)),
        Step(RunTestCase("获取可申请发票订单").call(getInvoiceApply).export(*["bdSubOrderId", "itemCode","learnId","itemName", "grade", "payment","invoiceType"])),
        Step(RunTestCase("申请企业发票").call(ApplyRecord)),
        Step(RunTestCase("号码搜索发票列表").setup_hook('${login_web()}', "Cookie").call(invoiceApp_itemList).export(*["itemId", "itemName","Cookie"])),
        Step(RunTestCase("驳回发票申请").with_variables(**({"status":"2"})).call(invoiceApp_chageItemSatus)),
        Step(RunTestCase("获取申请列表的发票申请第一条是审核不通过").with_variables(**({"status":"2"})).call(getInvoiceApplyRecord)),


    ]

if __name__ == '__main__':
    TestApply_Record().test_start()