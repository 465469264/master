from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.selAppMsgCenter import selAppMsgCenter
from api.app.loginOrRegister import app_login
from api.app.updateInMessageRead import updateInMessageRead
#msgType:  1>学习提醒, 5>任务提醒,  6>账户通知 , 2>活动提醒  4>资讯头条,  3>系统提醒  ,8>@我   9>点赞   10>评论  ,11>粉丝
class TestCasesMsgCenter(HttpRunner):
    config = (
        Config("学员和老师账号返回的通知标题")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(accountnumber,teacher_student6)}",
        })
            )
    teststeps = [
        Step(RunTestCase("登录学员和老师账号").setup_hook('${delay(1)}').call(app_login).export(*["app_auth_token","userId"])),
        Step(RunTestCase("学员和老师账号返回的通知标题").setup_hook('${delay(1)}').call(selAppMsgCenter)),
        Step(RunTestCase("通知列表消息@我一键已读").setup_hook('${delay(1)}').with_variables(**({"a":"8"})).call(updateInMessageRead)),
        Step(RunTestCase("通知列表消息评论一键已读").setup_hook('${delay(1)}').with_variables(**({"a":"10"})).call(updateInMessageRead)),

                 ]

if __name__ == '__main__':
    TestCasesMsgCenter().test_start()