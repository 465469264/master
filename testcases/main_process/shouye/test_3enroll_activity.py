from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.addNewComment import addNewComment
from api.app.loginOrRegister import app_login
from api.app.usPraise import usPraise
from api.app.enrollUpwardAct import enrollUpwardAct
from api.app.userHome import get_inf0

from api.app.selAppMsgCenter import selAppMsgCenter

class Test_Enroll_Activity(HttpRunner):
    config = (
        Config("报名-点赞-评论活动")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(accountnumber,teacher_student6)}",
            "content": "测试测试测试",
            "mappingId": "${read_data_number(activity,mappingId)}",
            "praiseId":"${read_data_number(activity,mappingId)}",
            "message" : "success",
            "ifLimit": "0"

})
    )
    teststeps = [
        Step(RunTestCase("登录测试账号").setup_hook('${delay(1)}').call(app_login).teardown_hook('${delete_activity($userId)}').export(*["app_auth_token","userId"])),
        Step(RunTestCase("获取用户信息").call(get_inf0).export(*["nickname", "realName", "stdName"])),
        Step(RunTestCase("点赞活动").with_variables(**({"praiseType": "2","fabulousNum": "1"})).setup_hook('${delay(1)}').call(usPraise)),
        Step(RunTestCase("取消点赞活动").with_variables(**({"praiseType": "2","fabulousNum": "-1"})).call(usPraise)),
        Step(RunTestCase("评论活动-正常评论").with_variables(**({"commentType" :"3","circleUserId":"","userName":""})).call(addNewComment)),
        Step(RunTestCase("评论活动-评论字数100个字").with_variables(**({"commentType": "3", "circleUserId": "","mobile":"","userId":"","userName":"","content": "热评外显，默认取动态中点赞最高评论放在外面显示，"
                                                                                                                           "只显示一条；且评论的点赞数要达到>>5个赞才显示在列表外；"
                                                                                                                           "如果某条动态热评最高的点赞只有4个赞，则这条热评不外显在列表外,"
                                                                                                                           "动态详情的评论增加按热度的排序，默认按热度排序,按热度排：点赞从"
                                                                                                                           "高到低排列（评论都没有人点赞时，则按照评论的时间排序"})).call(addNewComment)),
        Step(RunTestCase("评论活动-为空评论").with_variables(**({"commentType": "3", "circleUserId": "", "mobile":"","userId":"","userName":"","content": "","message" : "评论的内容与图片不能同时为空"})).call(addNewComment)),
        Step(RunTestCase("报名活动").with_variables(**({"actId":"$praiseId"})).call(enrollUpwardAct)),
        Step(RunTestCase("校验消息中心是否收到了报名活动的消息通知").setup_hook('${delay(1)}').call(selAppMsgCenter).teardown_hook(
            '${selAppMsgCenter_msgtype2($body)}')),

    ]

if __name__ == '__main__':
    Test_Enroll_Activity().test_start()