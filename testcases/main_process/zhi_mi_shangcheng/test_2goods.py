from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.goodsList import goodsList
from api.app.goodsListAll import goodsListAll
from api.app.getVocationalCourseList import getVocationalCourseList

class Test_Apply_qita(HttpRunner):
    # @pytest.mark.parametrize("param",Parameters({"salesType-goodsType-message":"${salesType_goodsType()}"}))
    # def test_start(self,param):
    #     super().test_start(param)
    config = (
        Config("智米商城branner")
            .verify(False)
            .variables(**{
                            "pageSize": "20",
                            "pageNum": "1",
                            "createResource": "2",
                             "salesType": "1",                   #1>兑换活动  2>抽奖活动  3>竞价活动  4>生日活动
                            "goodsType": "1",                  #1>普通商品	 2>课程商品	3>活动商品	4>教材商品	 5>生日商品
                            "message": "success"
                         }
                       )
    )
    teststeps = [
        Step(RunTestCase("智米商城-商品列表").call(goodsList)),
        Step(RunTestCase("智米商城-所有商品").call(goodsListAll)),
        Step(RunTestCase("智米商城-培训课程列表").call(getVocationalCourseList)),

    ]
if __name__ == '__main__':
    Test_Apply_qita().test_start()