from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.editAddress import eddit_address
from api.app.mallConfirmOrder import buy_goods
from api.web.zhimi_give_toAdd_do import zhimi_token
from api.web.zhimi_give_getUserInfo_do import getUserInfo
from api.web.zhimi_give_add_do import zhimi_give
from api.web.zhimi_give_check_list_do import zhimi_give_check_list
from api.web.zhimi_give_check_toCheck_do import zhimi_check_token
from api.web.zhimi_give_check_check_do import check_zhimi
from api.app.loginOrRegister import app_login


class TestCasesbuy_zhimi_goods(HttpRunner):
    config = (
        Config("购买商城中纯智米商品")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(test_data,register_mobile)}"
        })
            )
    teststeps = [
        # 智米赠送申请
        Step(RunTestCase("取智米赠送的web_token").call(zhimi_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("获取用户信息，获取userId").call(getUserInfo).export(*["user_id"])),
        Step(RunTestCase("智米赠送").call(zhimi_give)),
        #智米赠送审核
        Step(RunTestCase("获取要审核的记录id").call(zhimi_give_check_list).export(*["id"])),
        Step(RunTestCase("获取智米审核web_token").call(zhimi_check_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("智米赠送").call(check_zhimi)),
        Step(RunTestCase("登录刚注册的手机号").call(app_login).export(*["app_auth_token", "userId"])),
        Step(RunTestCase("购物添加收获地址").call(eddit_address)),
        Step(RunTestCase("购物纯智米商品").call(buy_goods)),
    ]
if __name__ == '__main__':
    TestCasesbuy_zhimi_goods().test_start()