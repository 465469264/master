import pytest,sys,os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.addNewComment import addNewComment
from api.app.userHome import get_info

class Test_Enroll_Activity(HttpRunner):
    @pytest.mark.parametrize("param",Parameters({"title-content-message":"${Activity_content()}"}))
    def test_start(self,param):
        super().test_start(param)
    config = (
        Config("报名-点赞-评论活动")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(ApplyRecord,mobile)}",
            "mappingId": "${read_data_number(activity,mappingId)}",                        #活动id
            "ifLimit": "0",                                                               #0>能否连续评论
            "commentType": "3", "circleUserId": "", "userId": "", "userName": "",
        })
    )
    teststeps = [
        Step(RunTestCase("获取用户信息").call(get_info).teardown_hook('${delete_activity($userId)}').export(*["nickname", "realName", "stdName","userId"])),
        Step(RunTestCase("评论活动").call(addNewComment)),

    ]

if __name__ == '__main__':
    Test_Enroll_Activity().test_start()