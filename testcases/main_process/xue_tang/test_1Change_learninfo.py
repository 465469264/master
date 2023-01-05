from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.stdLearnInfo import stdLearnInfo
from api.app.getDefaultLearnInfo import getDefaultLearnInfo
from api.app.setDefaultLearnInfo import setDefaultLearnInfo

class Test_change_learn(HttpRunner):
    config = (
        Config("用户切换学籍")
            .verify(False)
            .variables(**{
                            "message": "success",
                            }
                       )

            )
    teststeps = [
        Step(RunTestCase("获取当前学籍信息").call(stdLearnInfo).export(*["learnId","learnId1"])),
        Step(RunTestCase("切换当前学籍").call(setDefaultLearnInfo)),
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId","learnId1"])),
        Step(RunTestCase("获取当前学籍信息").call(getDefaultLearnInfo).teardown_hook('${judge_learnId($learnId,$learnId1,$learnId_dangqian)}',"a").export(*["a"])),
        Step(RunTestCase("切换另外一个学籍").with_variables(**({"learnId":"$a"})).call(setDefaultLearnInfo)),

    ]
if __name__ == '__main__':
    Test_change_learn().test_start()