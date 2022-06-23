from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.editAddress import eddit_address
from api.app.mallConfirmOrder import buy_goods
from api.app.loginOrRegister import app_login
from api.app.getJDProvince import GetJDProvince
from api.app.getJDCity import getJDCity
from api.app.getJDCounty import getJDCounty
from api.app.editAddress import eddit_address

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
        Step(RunTestCase("获取省份").call(GetJDProvince).export(*["provinceCode", "provinceName"])),
        Step(RunTestCase("获取城市").with_variables(**({"id": "$provinceCode"})).call(getJDCity).export(*["cityCode", "cityName"])),
        Step(RunTestCase("地区").with_variables(**({"id": "$cityCode"})).call(getJDCounty).export(*["districtCode", "districtName"])),
        Step(RunTestCase("编辑收货地址").with_variables(**({"saName": "测试", "address": "测试地址", "saType": "3", "excType": "2", "email": "123@qq.com"})).call(eddit_address)),
        Step(RunTestCase("购物纯智米商品").call(buy_goods)),
    ]
if __name__ == '__main__':
    TestCasesbuy_zhimi_goods().test_start()