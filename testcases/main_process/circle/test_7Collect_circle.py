#收藏帖子-查看自己的收藏列表
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.userHome import get_info
from api.app.usCollect import usCollect,usCollect2
from api.app.selCircleCollects import selCircleCollects
from api.app.selCircleDynamicInfos import selCircleDynamicInfos


class Test_Circle_Dynamics(HttpRunner):
    config = (
        Config("收藏帖子-查看自己的收藏列表")
            .verify(False)
            .variables(**{
            "message": "success",
            "targetMobile": "",                    # 对象手机
            "targetRealName": "",                 # 对象名称
            "own": "",
            "pageSize": "20",
            "pageNum": "1",
            "userRoleType": "",
            "scType": "2",  # 读书社


        })
    )
    teststeps = [
        Step(RunTestCase("获取当前人的参数").call(get_info).export(*["userId"])),
        Step(RunTestCase("进入读书社圈子页").call(selCircleDynamicInfos).export(*["id"])),
        Step(RunTestCase("收藏第一条帖子").with_variables(**({"isCollects": "1","circleId": "$id"})).call(usCollect).export("body")),
        Step(RunTestCase("进入查看自己的收藏列表").call(selCircleDynamicInfos)),
        Step(RunTestCase("取消收藏第一条帖子").with_variables(**({"isCollects": "0", "circleId": "$id","id":"$body"})).call(usCollect2)),

    ]

if __name__ == "__main__":
    Test_Circle_Dynamics().test_start()



