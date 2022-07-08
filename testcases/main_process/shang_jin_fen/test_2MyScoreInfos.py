#上级分页面
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.userHome import get_info
from api.app.stdLearnInfo import stdLearnInfo
from api.app.presentTerm import presentTerm
from api.app.selScoreByTerm import selScoreByTerm
from api.app.gsMyScoreInfos import gsMyScoreInfos

class Test_Score_List(HttpRunner):
    config = (
        Config("我的上进分")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "pageSize": "5",
                            "pageNum": "1",
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取信息").call(get_info).export(*["userId"])),
        Step(RunTestCase("获取learnId").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("返回当前学期").call(presentTerm).export(*["body"])),
        Step(RunTestCase("根据学期统计上进分").with_variables(**({"term":"$body"})).call(selScoreByTerm).export(*["body"])),
        Step(RunTestCase("我的上进分-明细").setup_hook('${find_MyScoreInfos($userId)}', "behaviorDesc").with_variables(**({"term":"$body"})).call(gsMyScoreInfos)),

    ]

if __name__ == "__main__":
    Test_Score_List().test_start()



