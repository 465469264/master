#上级分页面
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.stdLearnInfo import stdLearnInfo
from api.app.presentTerm import presentTerm
from api.app.selScoreByTerm import selScoreByTerm
class Test_Score_List(HttpRunner):
    config = (
        Config("我的上进分")
            .verify(False)
            .variables(**{
                            "message": "success",
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取learnId").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("返回当前学期").call(presentTerm).export(*["body"])),
        Step(RunTestCase("根据学期统计上进分").with_variables(**({"term":"$body"})).call(selScoreByTerm).export(*["body"])),


    ]

if __name__ == "__main__":
    Test_Score_List().test_start()



