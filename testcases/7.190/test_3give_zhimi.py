from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.web.zhimi_give_toAdd_do import zhimi_token
from api.web.zhimi_give_getUserInfo_do import getUserInfo
from api.web.zhimi_give_add_do import zhimi_give
from api.web.zhimi_give_check_list_do import zhimi_give_check_list
from api.web.zhimi_give_check_toCheck_do import zhimi_check_token
from api.web.zhimi_give_check_check_do import check_zhimi
from api.web.login_web_test import login


class TestCasesbuy_give_zhimi(HttpRunner):
    config = (
        Config("赠送智米")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(test_data,register_mobile_chengjiao)}",
            "accType": "2",  # accType.1	>现金账户	 2>智米	 3>滞留账户
            "pageSize": "20",
            "pageNum": "1",
            "amount": "100",     # 100智米
            "a": "1",
            "zhimiType": "1",   #1>进账   2>出账
            "reasonStatus": "2",  # 2>通过   3>驳回
        })
            )
    teststeps = [
        # 智米赠送申请
        Step(RunTestCase("取智米赠送的web_token").setup_hook('${login_web()}', "Cookie").call(zhimi_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token","Cookie"])),
        Step(RunTestCase("获取用户信息，获取userId").call(getUserInfo).export(*["user_id"])),
        Step(RunTestCase("后台申请智米赠送100").with_variables(**({"zhimiCount":"$amount","accSerialType":"5","userId":"$user_id"})).call(zhimi_give)),
        #智米赠送审核
        Step(RunTestCase("获取要审核的记录id").call(zhimi_give_check_list).export(*["id"])),
        Step(RunTestCase("获取智米审核web_token").call(zhimi_check_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("智米赠送").call(check_zhimi)),
    ]

if __name__ == '__main__':
    a = login().login()
    TestCasesbuy_give_zhimi().test_start()