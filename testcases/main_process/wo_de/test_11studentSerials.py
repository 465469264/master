from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.getOrderList import getOrderList
from api.app.myBookOrder import myBookOrder
from api.app.stdLearnInfo import stdLearnInfo
from api.app.studentSerials import studentSerials
from api.app.getReceipt import getReceipt
from api.app.stuSerialsBySubOrderNo import stuSerialsBySubOrderNo

class Test_qiandao(HttpRunner):
    config = (
        Config("缴费管理")
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
        Step(RunTestCase("我的页面-缴费管理返回已缴费订单").call(studentSerials).export(*["subOrderNo"])),
        Step(RunTestCase("获取电子收据前-获取发票配置").call(getReceipt)),
        Step(RunTestCase("获取电子收据").call(stuSerialsBySubOrderNo)),

    ]
if __name__ == '__main__':
    Test_qiandao().test_start()