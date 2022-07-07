import pytest,sys,os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.selProblemList import selProblemList
from api.app.selProblemAnswer import selProblemAnswer

class Test_all_selProblemListo(HttpRunner):
    @pytest.mark.parametrize("param",Parameters({"title-channel-message":"${channel()}"}))
    def test_start(self,param):
        super().test_start(param)
    config = (
        Config("帮助与反馈页面")
            .verify(False)
            .variables(**{
                          })
            )
    teststeps = [
        Step(RunTestCase("帮助与反馈页面").call(selProblemList)),
    ]
if __name__ == '__main__':
    Test_all_selProblemListo().test_start()