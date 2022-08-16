from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.getInvoiceApply import getInvoiceApply



class TestCasesPay_fee(HttpRunner):
    config = (
        Config("编辑管理员")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables(**{
                "mobile": "${read_data_number(test_data,register_mobile_chengjiao)}"
                })
    )
    teststeps = [
        # 缴费辅导费,并生成学院订单
        # Step(RunTestCase("获取缴费信息,并生成学院订单").setup_hook('${login_web()}', "Cookie").call(querry).teardown_hook('${College_order($learn_Id)}').export(*["learnId","learn_Id","subOrderNo","grade","feeAmount","Cookie"])),
    ]

if __name__ == '__main__':
    a = login().login()
    TestCasesPay_fee().test_start()