#不同的圈子
import pytest,sys,os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from httprunner import HttpRunner, Config, Step, Parameters, RunTestCase
from api.app.selCircleDynamicInfos import selCircleDynamicInfos
from api.app.userHome import get_info
from api.app.addNewComment import addNewComment

class Test_Comment_circle_all(HttpRunner):
    @pytest.mark.parametrize("param",Parameters({"title-content-message":"${Activity_content()}"}))
    def test_start(self,param):
        super().test_start(param)
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
            "commentType":"4",
            "content": "测试测试",


        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取登陆人参数").with_variables(**({"message":"success"})).call(get_info).export(*["userId","nickname","realName","stdName"])),
        Step(RunTestCase("进入圈子页").with_variables(**({"message":"success"})).call(selCircleDynamicInfos).export(*["id"])),
        Step(RunTestCase("评论活动").with_variables(**({"mappingId": "$id","ifLimit":"0","circleUserId":"$userId","userName":""})).call(addNewComment)),
    ]
if __name__ == '__main__':
    Test_Comment_circle_all().test_start()



