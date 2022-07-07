#不同的圈子
from httprunner import HttpRunner, Config, Step, Parameters, RunTestCase
from api.app.selCircleDynamicInfos import selCircleDynamicInfos
from api.app.userHome import get_info
from api.app.selCircleDynamicsDetail import selCircleDynamicsDetail
from api.app.usReadOrForward import usReadOrForward
from api.app.getCommentInfo import getCommentInfo
from api.app.addNewComment import addNewComment
from api.app.usPraise import usPraise

class Test_circle_type(HttpRunner):
    config = (
        Config("搜索接口搜索不同类型")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(ApplyRecord,mobile)}",
            "own": "",
            "pageSize": "20",
            "pageNum": "1",
            "userRoleType": "",
            "scType": "2",               #读书社
            "sortOrder": "2",            #评论按时间排序
            "content": "测试测试",
            "commentType":"4",
            "message": "success"
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取登陆人参数").call(get_info).export(*["userId","nickname","realName","stdName"])),
        Step(RunTestCase("进入圈子页").call(selCircleDynamicInfos).export(*["id"])),
        Step(RunTestCase("查看列表第一条的圈子详情").call(selCircleDynamicsDetail)),
        Step(RunTestCase("查看圈子返回附近的人").with_variables(**({"mappingId": "$id","heatType": "3","type": "1","readNum": "1"})).call(usReadOrForward)),
        Step(RunTestCase("评论活动").with_variables(**({"mappingId": "$id","ifLimit":"0","circleUserId":"$userId","userName":""})).call(addNewComment)),
        Step(RunTestCase("获取圈子的评论与刚刚的评论一致").with_variables(**({"a":"0","mappingType":"4","mappingId":"$id",})).call(getCommentInfo).export(*["commentId"])),
        Step(RunTestCase("点赞第一条评论").with_variables(**({"praiseType": "5", "fabulousNum": "1", "praiseId": "$commentId"})).call(usPraise)),
        Step(RunTestCase("取消点赞第一条评论").with_variables(**({"praiseType": "5", "fabulousNum": "-1", "praiseId": "$commentId"})).setup_hook('${delay(1)}').call(usPraise)),
        Step(RunTestCase("点赞帖子").with_variables(**({"praiseType": "3","fabulousNum":1,"praiseId": "$id"})).call(usPraise)),
        Step(RunTestCase("取消点赞帖子").with_variables(**({"praiseType": "3","fabulousNum": -1, "praiseId": "$id"})).call(usPraise)),

    ]

if __name__ == "__main__":
    Test_circle_type().test_start()



