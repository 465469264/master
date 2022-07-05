#圈子页的活动
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.selTaskClockRecommend import selTaskClockRecommend
from api.app.userHome import get_info
from api.app.selClockTaskDetails import selClockTaskDetails
from api.app.selClockTaskRecords import selClockTaskRecords
from api.app.selCircleDynamicInfos import selCircleDynamicInfos
from api.app.usTaskClockRanking import usTaskClockRanking
from api.app.usTaskClockRecord import usTaskClockRecord

class Test_circle_habbit(HttpRunner):
    config = (
        Config("习惯打卡里的接口")
            .verify(False)
            .variables(**{
            "pageSize": 20,
            "pageNum": 1,
            "own": "0",
            "scType": "3",
            "userRoleType": "",
            "message": "success"

        })
    )
    teststeps = [
        Step(RunTestCase("获取信息").call(get_info).export(*["nickname", "realName","stdName","userId"])),
        Step(RunTestCase("APP圈子活动页返回推荐的习惯").call(selTaskClockRecommend).export(*["id","name"])),
        Step(RunTestCase("查看第一个推荐的习惯详情").with_variables(**({"taskId":"$id"})).call(selClockTaskDetails)),
        Step(RunTestCase("查看打卡情况").with_variables(**({"taskId": "$id"})).call(selClockTaskRecords)),
        Step(RunTestCase("查看打卡记录").with_variables(**({"taskId": "$id"})).call(selCircleDynamicInfos)),
        Step(RunTestCase("打卡排行榜").with_variables(**({"taskId": "$id"})).call(usTaskClockRanking)),
        Step(RunTestCase("习惯任务-我的战绩").call(usTaskClockRecord)),

    ]

if __name__ == "__main__":
    Test_circle_habbit().test_start()



