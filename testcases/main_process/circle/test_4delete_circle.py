#圈子-动态页加载branner
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.selCircleDynamicInfos import selCircleDynamicInfos2
from api.app.userHome import get_info
from api.app.usSetDynamics import usSetDynamics

class Test_Delete_cicle(HttpRunner):
    config = (
        Config("删除自己的第一条帖子")
            .verify(False)
            .variables(**{
            "own": "0",
            "pageSize": 20,
            "userRoleType": "",
            "pageNum": 1,
            "status": "3",       #3>删除
    })
    )
    teststeps = [
        Step(RunTestCase("获取登陆人参数").call(get_info).export(*["userId"])),
        Step(RunTestCase("进入自己的主页").call(selCircleDynamicInfos2).export(*["id"])),
        Step(RunTestCase("删除自己的第一条圈子").with_variables(**({"circleUserId":"$userId"})).call(usSetDynamics)),

    ]

if __name__ == "__main__":
    Test_Delete_cicle().test_start()



