from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.selAppMsgCenter import selAppMsgCenter
from api.app.addNewComment import addNewComment
from api.app.userHome import get_info
from api.app.selCircleDynamicInfos import selCircleDynamicInfos2



#msgType:  1>学习提醒, 5>任务提醒,  6>账户通知 , 2>活动提醒  4>资讯头条,  3>系统提醒  ,8>@我   9>点赞   10>评论  ,11>粉丝
class TestCasesAddNewComment(HttpRunner):
    config = (
        Config("学员和老师账号返回的通知标题")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(ApplyRecord,mobile)}",
            "userRoleType": 2,
            "own": 1,
            "pageSize": 20,
            "pageNum": 1,
            "ifLimit": "0",
            "commentType": "4",          #评论圈子
            "content": "测试测试测试",
            "message": "success",

        })
    )
    teststeps = [
        Step(RunTestCase("账号返回的通知标题").call(selAppMsgCenter)),
        Step(RunTestCase("获取用户信息，获取userId").call(get_info).export(*["userId","realName","nickname","stdName"])),
        Step(RunTestCase("查看自己的圈子").call(selCircleDynamicInfos2).export(*["id"])),
        Step(RunTestCase("评论帖子").with_variables(**({"mappingId": "$id","mobile":"","circleUserId":"$userId","userId":"","userName":""})).call(addNewComment)),
        Step(RunTestCase("评论帖子-@人").with_variables(
            **({"mappingId": "$id","content": "@杨彬\b看看看看艾特你了","circleUserId":"$userId","userName":"$realName"})).call(
            addNewComment)),

    ]


if __name__ == '__main__':
    TestCasesAddNewComment().test_start()