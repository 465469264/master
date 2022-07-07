#习惯打卡列表
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.userHome import get_info
from api.app.selTodayClockTaskList import selTodayClockTaskList
from api.app.selClockTaskByType import selClockTaskByType
from api.app.selClockTaskTabInfos import selClockTaskTabInfos

class Test_circle_habbit(HttpRunner):
    config = (
        Config("习惯打卡列表")
            .verify(False)
            .variables(**{
                            "message":"success",
                            "name": "amylee跑步测试勿删",         #今日可打卡的第一个习惯打卡名字
                            "pageNum": "1",
                            "pageSize": "20",
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("APP活动页-今日习惯打卡").call(selTodayClockTaskList)),
        Step(RunTestCase("APP活动页-进入读书习惯列表").with_variables(**({"type": "2","markTaskType":2})).call(selClockTaskByType)),
        Step(RunTestCase("读书习惯打卡列表参与人头像").with_variables(**({"type": "2","name": "读书"})).call(selClockTaskTabInfos)),
        Step(RunTestCase("APP活动页-进入跑步习惯列表").with_variables(**({"type": "3", "markTaskType": 3})).call(selClockTaskByType)),
        Step(RunTestCase("跑步习惯打卡列表参与人头像").with_variables(**({"type": "3","name": "跑步"})).call(selClockTaskTabInfos)),
        Step(RunTestCase("APP活动页-进入其他习惯列表").with_variables(**({"type": "4", "markTaskType": 4})).call(selClockTaskByType)),
        Step(RunTestCase("其他习惯打卡列表参与人头像").with_variables(**({"type": "4","name": "其他"})).call(selClockTaskTabInfos)),

    ]

if __name__ == "__main__":
    Test_circle_habbit().test_start()



