from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.selAppMsgCenter import selAppMsgCenter
from api.app.addNewComment import addNewComment
from api.app.loginOrRegister import app_login
from api.app.userHome import get_info


#msgType:  1>学习提醒, 5>任务提醒,  6>账户通知 , 2>活动提醒  4>资讯头条,  3>系统提醒  ,8>@我   9>点赞   10>评论  ,11>粉丝
class TestCasesAddNewComment(HttpRunner):
    config = (
        Config("学员和老师账号返回的未读数量")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(accountnumber,teacher_student6)}",
            "mappingId": "${read_data_number(circle,mappingId)}",
            "circleUserId": "${read_data_number(circle,circleUserId)}",
            "message": "success"
        })
    )
    teststeps = [
        Step(RunTestCase("登录老师账号").with_variables(**({"mobile": "${read_data_number(accountnumber,teacher2)}"})).call(app_login).export(*["app_auth_token"])),
        Step(RunTestCase("老师账号返回的通知标题").call(selAppMsgCenter)),
        Step(RunTestCase("获取用户信息").call(get_info).export(*["nickname","realName","stdName"])),
        Step(RunTestCase("评论帖子").with_variables(**({"commentType" :"4","ifLimit": "0","content": "嗨，1，测试a##￥","mobile":"","userId":"","userName":""})).call(addNewComment)),
        Step(RunTestCase("评论帖子-@人").with_variables(**({"commentType": "4", "ifLimit": "0", "content": "@杜建航\b看看看","userId":"$circleUserId","userName":"杜建航"})).call(addNewComment)),

    ]


if __name__ == '__main__':
    TestCasesAddNewComment().test_start()