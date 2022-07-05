from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.mallConfirmOrder import mallConfirmOrder
from api.app.stuItemToPay import stuItemToPay
from api.app.goodsListAll import goodsListAll
from api.app.goodsDetail import goodsDetail
from api.app.getOrderList import getOrderList
from api.app.addComment import addComment
from api.app.goodsComment import goodsComment
from api.app.goodsSalesRecords import goodsSalesRecords
from api.app.getAccountBalance import getAccountBalance
from api.app.editAddress import eddit_address
from api.app.getJDProvince import GetJDProvince
from api.app.getJDCity import getJDCity
from api.app.getJDCounty import getJDCounty
from api.app.getJDTown import getJDTown
from api.app.myAddress import myAddress


class TestCasesbuy_zhimi_goods(HttpRunner):
    config = (
        Config("购买商城中纯智米商品")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(ApplyRecord,mobile)}",
            "salesType": "1",  # 1>兑换活动  2>抽奖活动  3>竞价活动  4>生日活动
            "pageSize": "20",
            "pageNum": "1",
            "goodsType": "1",
            "message":"success",
            "salesId": "165692420259338774",
            "saId": "66465",
            "commentContent": "测试测试",
            "exchangeCount": "1",  # 购买数量

        })
            )
    teststeps = [
        # 智米赠送申请
        Step(RunTestCase("获取我的地址").with_variables(**({"saType": "3"})).call(myAddress).export(*["saId"])),
        Step(RunTestCase("获取省份").call(GetJDProvince).export(*["provinceCode", "provinceName"])),
        Step(RunTestCase("获取城市").with_variables(**({"id": "$provinceCode"})).call(getJDCity).export(*["cityCode", "cityName"])),
        Step(RunTestCase("地区").with_variables(**({"id": "$cityCode"})).call(getJDCounty).export(*["districtCode", "districtName"])),
        Step(RunTestCase("乡镇").with_variables(**({"id": "$districtCode"})).call(getJDTown).export(*["streetCode", "streetName"])),
        Step(RunTestCase("编辑收货地址").with_variables(**({"saName": "测试", "address": "测试地址", "saType": "3", "excType": "2", "email": "123@qq.com"})).call(eddit_address)),
        Step(RunTestCase("智米商城-所有商品").call(goodsListAll)),
        Step(RunTestCase("智米商城-查看商品详情").call(goodsDetail)),
        Step(RunTestCase("智米商城-评论商品").call(addComment)),
        Step(RunTestCase("智米商城-查看商品的评论").call(goodsComment)),
        Step(RunTestCase("智米商城-查看商品的兑换记录").call(goodsSalesRecords)),
        Step(RunTestCase("智米商城-获取账余额").call(getAccountBalance)),
        Step(RunTestCase("购物纯智米商品-生成订单").call(mallConfirmOrder).export(*["body"])),
        Step(RunTestCase("智米商城-提交订单").with_variables(**({"mappingId": "$body","accDeduction": "0.0", "zmScale": "0", "payAmount": "0.0","zmDeduction": "0", "payItem": "mallRedemption", })).call(stuItemToPay)),
        Step(RunTestCase("查看商品订单").call(getOrderList)),

    ]
if __name__ == '__main__':
    TestCasesbuy_zhimi_goods().test_start()