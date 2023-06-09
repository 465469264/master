from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.selProblemList import selProblemList
from api.app.selProblemAnswer import selProblemAnswer

class Test_selProblemListo(HttpRunner):
    config = (
        Config("帮助与反馈页面")
            .verify(False)
            .variables(**{
                "message": "success",
                "channel": "1"
                          })
            )
    teststeps = [
        Step(RunTestCase("帮助与反馈页面").call(selProblemList).export(*["id"])),
        Step(RunTestCase("帮助与反馈页面第一个问题的答案").call(selProblemAnswer)),

    ]
if __name__ == '__main__':
    Test_selProblemListo().test_start()