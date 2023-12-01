import pytest,sys,os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
print(str(Path(__file__).parent.parent.parent.parent))
from httprunner import HttpRunner, Config, Step, Parameters, RunTestCase
from api.app.inMessageList import inMessageList

class Test_inMessageList(HttpRunner):
    @pytest.mark.parametrize("param",Parameters({"title-msgType-msgTitle":"${inMessageList()}"}))
    def test_start(self,param):
        super().test_start(param)
    config = (
        Config("消息中心>进入@我，点赞，评论,粉丝")
            .verify(False)
            .variables(**{
                            "pageNum": "1",
                            "pageSize": "20",
                            "message": "success",
                         }
                       )
    )
    teststeps = [
        Step(RunTestCase("消息中心>进入@我，点赞，评论,粉丝").call(inMessageList)),
    ]

if __name__ == '__main__':
    Test_inMessageList().test_start()

