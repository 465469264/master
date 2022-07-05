from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.loginOrRegister import app_login
from api.app.accountDetail import AccountDetail
from api.web.zhimi_give_add_do import zhimi_give
from api.web.zhimi_give_check_list_do import zhimi_give_check_list
from api.web.zhimi_give_check_toCheck_do import zhimi_check_token
from api.web.zhimi_give_check_check_do import check_zhimi
from api.web.zhimi_give_toAdd_do import zhimi_token
from api.app.accountSerial import AccountSerial
from api.app.userHome import get_info

class Test_Apply_qita(HttpRunner):
    config = (
        Config("智米支出页面")
            .verify(False)
            .variables(**{
                "mobile": "${read_data_number(ApplyRecord,mobile)}",
                "accType":"2",    #accType.1	>现金账户	 2>智米	 3>滞留账户
                "pageSize":"20",
                "pageNum":"1",
                "amount":"100",
                "a":"1",
                "zhimiType":"2",            #1>进账   2>出账
                "reasonStatus": "2",  # 2>通过   3>驳回
                "message": "success",

        })
    )
    teststeps = [
        Step(RunTestCase("获取信息").call(get_info).export(*["userId"])),
        Step(RunTestCase("取智米支出的web_token").setup_hook('${login_web()}', "Cookie").call(zhimi_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token","Cookie"])),
        Step(RunTestCase("后台申请智米支出100").with_variables(**({"zhimiCount":"$amount","accSerialType":"26"})).call(zhimi_give)),
        Step(RunTestCase("获取要审核的记录id").call(zhimi_give_check_list).export(*["id"])),
        Step(RunTestCase("获取智米审核web_token").call(zhimi_check_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("智米通过审核后支出").with_variables(**({"reasonStatus":"2"})).call(check_zhimi)),
        Step(RunTestCase("统计智米，并与数据库校验").setup_hook('${find_zhimi($userId)}', "accAmount").call(AccountDetail)),
        Step(RunTestCase("我的页面增加了一条100智米的支出记录").call(AccountSerial)),

    ]
if __name__ == '__main__':
    Test_Apply_qita().test_start()