from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.addNewComment import addNewComment
from api.app.selCircleDynamicInfos import selCircleDynamicInfos2
from api.app.userHome import get_info
import sys

#msgType:  1>学习提醒, 5>任务提醒,  6>账户通知 , 2>活动提醒  4>资讯头条,  3>系统提醒  ,8>@我   9>点赞   10>评论  ,11>粉丝
class TestCasesAddNewComment(HttpRunner):
    config = (
        Config("学员和老师账号返回的未读数量")
            .verify(False)
            .variables(**{
                        "userRoleType": "",
                        "own": 1,
                        "pageSize": 20,
                        "pageNum": 1,
                        "mobile": "${read_data_number(ApplyRecord,mobile)}",
                        "commentType": "4", "ifLimit": "0",
                        "message": "success"
                            }
                       )
                )
    teststeps = [
        Step(RunTestCase("获取用户信息").call(get_info).export(*["nickname","realName","stdName","userId"])),
        Step(RunTestCase("查看自己的圈子").call(selCircleDynamicInfos2).export(*["id"])),
        Step(RunTestCase("评论帖子").with_variables(**({"mappingId":"$id","circleUserId": "$userId","content": "嗨，1，测试a##￥","mobile":"","userId":"","userName":""})).call(addNewComment)),
        Step(RunTestCase("评论帖子-@人").with_variables(**({"mappingId":"$id","circleUserId": "$userId","content": "@杨彬\b看看看","userName":"杨彬"})).call(addNewComment)),

    ]


if __name__ == '__main__':
    TestCasesAddNewComment().test_start()