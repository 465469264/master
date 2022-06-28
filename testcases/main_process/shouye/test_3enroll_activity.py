import pytest,sys,os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.addNewComment import addNewComment
from api.app.usPraise import usPraise
from api.app.enrollUpwardAct import enrollUpwardAct
from api.app.userHome import get_info

from api.app.selAppMsgCenter import selAppMsgCenter

class Test_Enroll_Activity(HttpRunner):
    @pytest.mark.parametrize("param",Parameters({"content":"${Activity_content()}"}))
    def test_start(self,param):
        super().test_start(param)
    config = (
        Config("报名-点赞-评论活动")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(ApplyRecord,mobile)}",
            "praiseType": "2",            #2>活动点赞
            "mappingId": "${read_data_number(activity,mappingId)}",     #活动id
            "praiseId":"${read_data_number(activity,mappingId)}",
            "message" : "success",
            "ifLimit": "0",                                             #0>能否连续评论
            "commentType": "3", "circleUserId": "", "userId": "", "userName": "",

})
    )
    teststeps = [
        Step(RunTestCase("获取用户信息").call(get_info).teardown_hook('${delete_activity($userId)}').export(*["nickname", "realName", "stdName","userId"])),
        Step(RunTestCase("点赞活动").with_variables(**({"fabulousNum": "1"})).call(usPraise)),
        Step(RunTestCase("取消点赞活动").with_variables(**({"fabulousNum": "-1"})).setup_hook('${delay(1)}').call(usPraise)),
        Step(RunTestCase("评论活动").call(addNewComment)),
        Step(RunTestCase("报名活动").with_variables(**({"actId":"$praiseId"})).call(enrollUpwardAct)),
        Step(RunTestCase("校验消息中心是否收到了报名活动的消息通知").setup_hook('${delay(1)}').call(selAppMsgCenter).teardown_hook(
            '${selAppMsgCenter_msgtype2($body)}')),

    ]

if __name__ == '__main__':
    Test_Enroll_Activity().test_start()