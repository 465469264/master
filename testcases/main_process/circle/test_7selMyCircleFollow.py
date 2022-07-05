#关注列表跳转到关注的人的主页
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.selMyCircleFollowList import SelMyCircleFollowList
from api.app.userHome import get_info
from api.app.personalHomepageStatistics import personalHomepageStatistics

class Test_Circle_Dynamics(HttpRunner):
    config = (
        Config("关注列表跳转到关注的人的主页")
            .verify(False)
            .variables(**{
            "targetMobile": "",                    # 对象手机
            "targetRealName": "",                 # 对象名称
            "message": "success"

        })
    )
    teststeps = [
        Step(RunTestCase("获取当前人的参数").call(get_info).export(*["userId"])),
        Step(RunTestCase("关注列表").call(SelMyCircleFollowList).export(*["targetUserId","targetRealName"])),
        Step(RunTestCase("查看关注人的主页").with_variables(**({"userId":"$targetUserId"})).call(personalHomepageStatistics)),

    ]

if __name__ == "__main__":
    Test_Circle_Dynamics().test_start()



