#我的圈子
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.loginOrRegister import app_login
from api.app.stdLearnInfo import stdLearnInfo
from api.app.selCircleDynamicInfos import selCircleDynamicInfos


class TestCaseCircle_Dynamics_post(HttpRunner):
    config = (
        Config("查看自己的圈子动态")
            .verify(False)
            .variables(**{
             "mobile": "${read_data_number(ApplyRecord,mobile)}",
                "scType": "",
                "own": "",
        })
    )
    teststeps = [
            Step(RunTestCase("获取学员学业信息").call(stdLearnInfo).export("learnId","unvsId")),
            Step(RunTestCase("查看自己的圈子").with_variables(**({"pageSize":"20","userRoleType":2,"pageNum":1,"userId":"$unvsId"})).call(selCircleDynamicInfos)),



        ]

if __name__ == "__main__":
    TestCaseCircle_Dynamics_post().test_start()

