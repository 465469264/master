from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.selCommonMarketMenu import selCommonMarketMenu
from api.app.stdLearnInfo import stdLearnInfo
from api.app.usStudyReport import usStudyReport
from api.app.selLearnPageTip import selLearnPageTip

class Test_xuetang_table(HttpRunner):
    config = (
        Config("学堂页")
            .verify(False)
            .variables(**{
                            "message": "success",
                            }
                       )
            )
    teststeps = [
        Step(RunTestCase("获取学堂页二级菜单").with_variables(**({"level": "2","menuType": "2"})).call(selCommonMarketMenu)),
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("我的学习报告").call(usStudyReport)),
        Step(RunTestCase("学堂页的不知道什么接口").call(selLearnPageTip)),

    ]
if __name__ == '__main__':
    Test_xuetang_table().test_start()