#圈子页习惯打卡
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.selTaskClockRecommend import selTaskClockRecommend
from api.app.userHome import get_info
from api.app.selClockTaskDetails import selClockTaskDetails
from api.app.selClockTaskRecords import selClockTaskRecords
from api.app.selCircleDynamicInfos import selCircleDynamicInfos3
from api.app.selCircleDynamicInfos import selCircleDynamicInfos4
from api.app.usTaskClockRanking import usTaskClockRanking
from api.app.usTaskClockRecord import usTaskClockRecord
from api.app.usCancelSubscribe import usCancelSubscribe

class Test_circle_habbit(HttpRunner):
    config = (
        Config("活动页-返回的习惯选取第一个-习惯的详情及打卡情况，记录，战绩")
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
        # Step(RunTestCase("查看打卡情况").with_variables(**({"taskId": "$id"})).call(selClockTaskRecords)),
        Step(RunTestCase("查看所有的打卡记录").with_variables(**({"taskId": "$id"})).call(selCircleDynamicInfos3)),
        Step(RunTestCase("查看自己的打卡记录").with_variables(**({"taskId": "$id"})).call(selCircleDynamicInfos4)),
        Step(RunTestCase("打卡排行榜").with_variables(**({"taskId": "$id"})).call(usTaskClockRanking)),
        Step(RunTestCase("习惯任务-我的战绩").call(usTaskClockRecord)),
        Step(RunTestCase("习惯任务-关闭打卡提醒").with_variables(**({"status": "0"})).call(usCancelSubscribe)),
        Step(RunTestCase("习惯任务-开启打卡提醒").with_variables(**({"status": "1"})).call(usCancelSubscribe)),

    ]

if __name__ == "__main__":
    Test_circle_habbit().test_start()



