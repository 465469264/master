from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.web.zhimi_give_toAdd_do import zhimi_token
from api.app.userHome import get_info
from api.web.zhimi_give_add_do import zhimi_give
from api.web.zhimi_give_check_list_do import zhimi_give_check_list
from api.web.zhimi_give_check_toCheck_do import zhimi_check_token
from api.web.zhimi_give_check_check_do import check_zhimi


class TestCasesbuy_give_zhimi(HttpRunner):
    config = (
        Config("赠送智米")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(ApplyRecord,mobile)}",
            "accType": "2",  # accType.1	>现金账户	 2>智米	 3>滞留账户
            "pageSize": "20",
            "pageNum": "1",
            "amount": "100",     # 100智米
            "a": "1",
            "zhimiType": "1",   #1>进账   2>出账
            "reasonStatus": "2",  # 2>通过   3>驳回
            "message": "success",
                        }
                       )
            )
    teststeps = [
        # 智米赠送申请
        Step(RunTestCase("取智米赠送的web_token").setup_hook('${login_web()}', "Cookie").call(zhimi_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token","Cookie"])),
        Step(RunTestCase("获取用户信息，获取userId").setup_hook('${delay(1)}').call(get_info).export(*["userId"])),
        Step(RunTestCase("后台申请智米赠送100").with_variables(**({"zhimiCount":"$amount","accSerialType":"5",})).call(zhimi_give)),
        #智米赠送审核
        Step(RunTestCase("获取要审核的记录id").setup_hook('${delay(1)}').call(zhimi_give_check_list).export(*["id"])),
        Step(RunTestCase("获取智米审核web_token").call(zhimi_check_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("智米赠送").call(check_zhimi)),
    ]

if __name__ == '__main__':
    TestCasesbuy_give_zhimi().test_start()