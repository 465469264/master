from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.web.zhimi_give_toAdd_do import zhimi_token
from api.app.userHome import get_info
from api.web.zhimi_give_add_do import zhimi_give
from api.web.zhimi_give_check_list_do import zhimi_give_check_list
from api.web.zhimi_give_check_toCheck_do import zhimi_check_token
from api.web.zhimi_give_check_check_do import check_zhimi
from api.web.login_web_test import login
from api.app.loginOrRegister import app_login
from api.app.selAppMsgCenter import selAppMsgCenter


class TestCasesbuy_zhimi_goods(HttpRunner):
    config = (
        Config("智米推送")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(ApplyRecord,mobile)}",
            "zhimiType": "1",  # 1>进账   2>出账
            "amount": "100",  # 100智米
            "reasonStatus": "2",  # 2>通过   3>驳回
            "message": "success",

        })
            )
    teststeps = [
        # 智米赠送申请
        Step(RunTestCase("取智米赠送的web_token").setup_hook('${login_web()}', "Cookie").call(zhimi_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token","Cookie"])),
        Step(RunTestCase("获取用户信息，获取userId").call(get_info).export(*["userId"])),
        Step(RunTestCase("后台申请智米赠送100").with_variables(**({"zhimiCount":"$amount","accSerialType":"5",})).call(zhimi_give)),
        #智米赠送审核
        Step(RunTestCase("获取要审核的记录id").call(zhimi_give_check_list).export(*["id"])),
        Step(RunTestCase("获取智米审核web_token").call(zhimi_check_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("智米赠送审核").call(check_zhimi)),
        Step(RunTestCase("查看智米是否有推送").call(selAppMsgCenter)),
    ]
if __name__ == '__main__':
    a = login().login()
    TestCasesbuy_zhimi_goods().test_start()