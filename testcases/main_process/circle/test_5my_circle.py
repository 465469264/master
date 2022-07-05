#我的圈子
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.userHome import get_info
from api.app.selCircleDynamicInfos import selCircleDynamicInfos2


class TestCaseCircle_Dynamics_post(HttpRunner):
    config = (
        Config("查看自己的圈子动态")
            .verify(False)
            .variables(**{
                "userRoleType": 2,
                "own": 1,
                "pageSize": 20,
                "pageNum": 1,
                "message": "success"
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取用户信息，获取userId").call(get_info).export(*["userId"])),
        Step(RunTestCase("查看自己的圈子").call(selCircleDynamicInfos2)),



        ]

if __name__ == "__main__":
    TestCaseCircle_Dynamics_post().test_start()

