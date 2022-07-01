from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.selAppMsgCenter import selAppMsgCenter
from api.app.loginOrRegister import app_login
#msgType:  1>学习提醒, 5>任务提醒,  6>账户通知 , 2>活动提醒  4>资讯头条,  3>系统提醒  ,8>@我   9>点赞   10>评论  ,11>粉丝
class TestCasesnewUnReadNum(HttpRunner):
    config = (
        Config("评论和@的newUnReadNum的返回数据")
            .verify(False)
            .variables(**{
        })
            )
    teststeps = [

        Step(RunTestCase("判断消息通知@和评论的newUnReadNum").call(selAppMsgCenter).teardown_hook('${judge_newUnReadNum($newUnReadNum7)')),
                 ]

if __name__ == '__main__':
    TestCasesnewUnReadNum().test_start()