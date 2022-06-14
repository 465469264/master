from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.editAddress import eddit_address
from api.app.mallConfirmOrder import buy_goods
from api.app.loginOrRegister import app_login


class TestCasesbuy_zhimi_goods(HttpRunner):
    config = (
        Config("购买商城中纯智米商品")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(test_data,register_mobile_chengjiao)}"
        })
            )
    teststeps = [
        # 智米赠送申请
        Step(RunTestCase("登录刚注册的手机号").call(app_login).export(*["app_auth_token", "userId"])),
        Step(RunTestCase("购物添加收获地址").call(eddit_address)),
        Step(RunTestCase("购物纯智米商品").call(buy_goods)),
    ]
if __name__ == '__main__':
    TestCasesbuy_zhimi_goods().test_start()