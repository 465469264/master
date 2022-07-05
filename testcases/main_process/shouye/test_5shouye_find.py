#搜索不同类型
import pytest,sys,os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
print(str(Path(__file__).parent.parent.parent.parent))

from httprunner import HttpRunner, Config, Step, Parameters, RunTestCase
from api.app.getSearchList import getSearchList

class Test_shouye_find(HttpRunner):
    @pytest.mark.parametrize("param",Parameters({"keyWords-type":"${search()}"}))
    def test_start(self,param):
        super().test_start(param)
    config = (
        Config("搜索接口搜索不同类型")
            .verify(False)
            .variables(**{
                            "message": "success"
                         }
                       )
    )
    teststeps = [
        Step(RunTestCase("首页搜索").call(getSearchList)),

    ]

if __name__ == "__main__":
    Test_shouye_find().test_start()



