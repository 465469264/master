import pytest,sys,os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
print(str(Path(__file__).parent.parent.parent.parent))

from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.selProblemList import selProblemList
from api.app.selProblemAnswer import selProblemAnswer

class Test_selProblemListo(HttpRunner):
    @pytest.mark.parametrize("param",Parameters({"channel-message":"${channel()}"}))
    def test_start(self,param):
        super().test_start(param)
    config = (
        Config("帮助与反馈页面")
            .verify(False)
            .variables(**{
            "id": "",
                          })
            )
    teststeps = [
        Step(RunTestCase("帮助与反馈页面").call(selProblemList).export(*["id"])),
        Step(RunTestCase("帮助与反馈页面第一个问题的答案").call(selProblemAnswer)),

    ]
if __name__ == '__main__':
    Test_selProblemListo().test_start()