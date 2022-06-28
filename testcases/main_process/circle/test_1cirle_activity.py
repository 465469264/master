#圈子页的活动
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.selUpwardActivityInfo import selUpwardActivityInfo
from api.app.enrollUpwardAct import enrollUpwardAct
from api.app.selMyUpwardActivityInfo import selMyUpwardActivityInfo
from api.app.upwardActShare import upwardActShare
from api.app.addNewComment import addNewComment
from api.app.getCommentInfo import getCommentInfo
from api.app.userHome import get_info

class TestCaseCircle_Dynamics_post(HttpRunner):
    config = (
        Config("圈子页的活动报名-点赞，评论，查看我的活动")
            .verify(False)
            .variables(**{
             "mobile": "${read_data_number(ApplyRecord,mobile)}",
            "content": "测试测试",
        })
    )
    teststeps = [
        Step(RunTestCase("获取信息").call(get_info).teardown_hook('${delete_activity($userId)}').export(*["nickname", "realName","stdName","userId"])),
        Step(RunTestCase("获取圈子页的活动").call(selUpwardActivityInfo).export(*["id","actName"])),
        Step(RunTestCase("报名活动").with_variables(**({"actId": "$id"})).call(enrollUpwardAct)),
        Step(RunTestCase("查看我的活动页，报名成功").with_variables(**({"type":1,"pageSize":10,"pageNum":1,"a":0})).call(selMyUpwardActivityInfo)),
        Step(RunTestCase("分享活动").with_variables(**({"actId": "$id"})).call(upwardActShare)),
        Step(RunTestCase("评论").with_variables(**({"message":"success","mappingId":"$id","ifLimit": 0,"commentType": "3","circleUserId": "","userName":"$realName"})).call(addNewComment)),
        Step(RunTestCase("查看活动的评论").with_variables(**({"a":0,"pageSize": "15", "sortOrder": "","pageNum": 1, "mappingType": "3", "mappingId": "$id"})).call(getCommentInfo)),

    ]

if __name__ == "__main__":
    TestCaseCircle_Dynamics_post().test_start()



