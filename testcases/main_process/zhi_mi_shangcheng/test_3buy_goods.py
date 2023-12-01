from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.mallConfirmOrder import mallConfirmOrder
from api.app.stuItemToPay import stuItemToPay
from api.app.getOrderList import getOrderList



class Test_buy_goods(HttpRunner):
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
            "exchangeCount": "1",  # 购买数量

        })
            )
    teststeps = [
        # 智米赠送申请
        Step(RunTestCase("购物纯智米商品-生成订单").call(mallConfirmOrder).export(*["body"])),
        Step(RunTestCase("智米商城-提交订单").with_variables(**({"mappingId": "$body","accDeduction": "0.0", "zmScale": "0", "payAmount": "0.0","zmDeduction": "0", "payItem": "mallRedemption", })).call(stuItemToPay)),
        Step(RunTestCase("查看商品订单").call(getOrderList)),

    ]
if __name__ == '__main__':
    Test_buy_goods().test_start()