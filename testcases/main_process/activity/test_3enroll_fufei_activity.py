#报名付费活动
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.createUpwardActOrder import createUpwardActOrder
from api.app.stdLearnInfo import stdLearnInfo
from api.web.zhimi_give_add_do import zhimi_give
from api.web.zhimi_give_check_list_do import zhimi_give_check_list
from api.web.zhimi_give_check_toCheck_do import zhimi_check_token
from api.web.zhimi_give_check_check_do import check_zhimi
from api.web.zhimi_give_toAdd_do import zhimi_token
from api.app.accountDetail import AccountDetail
from api.app.userHome import get_info
from api.app.createUpwardActOrder import createUpwardActOrder

class Test_enroll_fufei_activity(HttpRunner):
    config = (
        Config("生成活动付费订单-缴费")
            .verify(False)
            .variables(**{
                        "mobile": "${read_data_number(ApplyRecord,mobile)}",
                        "actId": "205",
                        "accType": "2",  # accType.1	>现金账户	 2>智米	 3>滞留账户
                        "zhimiType": "1",  # 1>进账   2>出账
                        "reasonStatus": "2",  # 2>通过   3>驳回
                        "amount": "100",  # 100智米,
                        "payType": 17,       #支付类型：17
                        "tradeType": "APP",    #付费方，APP,H5等


    })
    )
    teststeps = [
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("生成活动缴费订单").call(createUpwardActOrder).export(*["body"])),
        Step(RunTestCase("获取信息").call(get_info).export(*["userId"])),
        Step(RunTestCase("取智米赠送的web_token").setup_hook('${login_web()}', "Cookie").call(zhimi_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token","Cookie"])),
        Step(RunTestCase("获取用户信息，获取userId").call(get_info).teardown_hook('${delete_activity($userId)}').export(*["userId"])),
        Step(RunTestCase("后台申请智米赠送100").with_variables(**({"zhimiCount":"$amount","accSerialType":"5",})).call(zhimi_give)),
        Step(RunTestCase("获取要审核的记录id").call(zhimi_give_check_list).export(*["id"])),
        Step(RunTestCase("获取智米审核web_token").call(zhimi_check_token).teardown_hook('${get_html($body)}',"_web_token").export(*["_web_token"])),
        Step(RunTestCase("智米赠送").call(check_zhimi)),

        Step(RunTestCase("用智米抵扣支付").with_variables(**({"amount": "0.00",  "zmDeduction": "100", "accDeduction": "0.00","orderNo": "$body",})).call(AccountDetail)),

    ]

if __name__ == "__main__":
    Test_enroll_fufei_activity().test_start()



