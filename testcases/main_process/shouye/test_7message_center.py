from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.loginOrRegister import app_login
from api.app.userHome import get_info
from api.app.addNewComment import addNewComment
from api.app.updateInMessageRead import updateInMessageRead
from api.app.selAppMsgCenter import selAppMsgCenter
#msgType:  1>学习提醒, 5>任务提醒,  6>账户通知 , 2>活动提醒  4>资讯头条,  3>系统提醒  ,8>@我   9>点赞   10>评论  ,11>粉丝

class TestCaseschicken_message(HttpRunner):
    config = (
        Config("消息一键已读-评论，@，点赞")
            .verify(False)
            .variables(**{
            "level":"2",
            "menuType":"1",
            "mappingId": "${read_data_number(circle,mappingId)}",
            "circleUserId": "${read_data_number(circle,circleUserId)}",

        })
            )
    teststeps = [
        Step(RunTestCase("通知列表-学习提醒-一键已读").with_variables(**({"a": "1"})).call(
            updateInMessageRead)),
        Step(RunTestCase("通知列表-活动提醒一键已读").with_variables(**({"a": "2"})).call(
            updateInMessageRead)),
        Step(RunTestCase("通知列表-系统提醒一键已读").with_variables(**({"a": "3"})).call(
            updateInMessageRead)),
        Step(RunTestCase("通知列表-资讯头条一键已读").with_variables(**({"a": "4"})).call(
            updateInMessageRead)),
        Step(RunTestCase("通知列表消息评论一键已读").with_variables(**({"a": "5"})).call(
            updateInMessageRead)),
        Step(RunTestCase("通知列表-任务提醒一键已读").with_variables(**({"a": "6"})).call(
            updateInMessageRead)),
        Step(RunTestCase("通知列表-@我一键已读").with_variables(**({"a": "8"})).call(
            updateInMessageRead)),
        Step(RunTestCase("通知列表-点赞一键已读").with_variables(**({"a": "9"})).call(
            updateInMessageRead)),
        Step(RunTestCase("通知列表-评论一键已读").with_variables(**({"a": "10"})).call(
            updateInMessageRead)),
        Step(RunTestCase("通知列表-粉丝一键已读").with_variables(**({"a": "11"})).call(
            updateInMessageRead)),
        Step(RunTestCase("获取用户信息").call(get_info).export(*["nickname", "realName", "stdName"])),
        Step(RunTestCase("老师账号返回的通知标题").call(selAppMsgCenter)),
                 ]

if __name__ == '__main__':
    TestCaseschicken_message().test_start()