import pytest,sys,os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
print(str(Path(__file__).parent.parent.parent.parent))

from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.selAppMsgCenter import selAppMsgCenter
from api.app.loginOrRegister import app_login
from api.app.updateInMessageRead import updateInMessageRead
#msgType:  1>学习提醒, 5>任务提醒,  6>账户通知 , 2>活动提醒  4>资讯头条,  3>系统提醒  ,8>@我   9>点赞   10>评论  ,11>粉丝
class TestCasesMsgCenter(HttpRunner):
    @pytest.mark.parametrize("param",Parameters({"msgType":"${msgType()}"}))
    def test_start(self,param):
        super().test_start(param)
    config = (
        Config("学员和老师账号返回的通知标题")
            .verify(False)
            .variables(**{
        })
            )
    teststeps = [
        Step(RunTestCase("学员和老师账号返回的通知标题").call(selAppMsgCenter)),
        Step(RunTestCase("通知列表消息一键已读").call(updateInMessageRead)),

                 ]

if __name__ == '__main__':
    TestCasesMsgCenter().test_start()