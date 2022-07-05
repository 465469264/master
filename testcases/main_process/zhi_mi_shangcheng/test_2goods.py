# import pytest,sys,os
# from pathlib import Path
# sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
# print(str(Path(__file__).parent.parent.parent.parent))

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
                            "salesType": "1", "goodsType": "1",
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