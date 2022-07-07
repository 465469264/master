from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.getOrderList import getOrderList
from api.app.myBookOrder import myBookOrder
from api.app.stdLearnInfo import stdLearnInfo

class Test_qiandao(HttpRunner):
    config = (
        Config("我的页面-我的订单")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "pageSize": 5,
                            "pageNum": 1,
                            }
                       )
            )
    teststeps = [
        Step(RunTestCase("学籍信息获取learnid").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("我的订单-商品订单").call(getOrderList)),
        Step(RunTestCase("我的订单-我的订单-教材订单").call(myBookOrder)),

    ]
if __name__ == '__main__':
    Test_qiandao().test_start()