#获取三个状态的活动
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.selUpwardActivityInfo import selUpwardActivityInfo


class Test_Circle_Dynamicst(HttpRunner):
    config = (
        Config("圈子页的活动报名-点赞，评论，查看我的活动")
            .verify(False)
            .variables(**{
                            "message": "success",
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取所有活动").with_variables(**({"type": ""})).call(selUpwardActivityInfo).export(*["id","actName"])),
        Step(RunTestCase("获取报名中活动").with_variables(**({"type": "1"})).call(selUpwardActivityInfo).export(*["id", "actName"])),
        Step(RunTestCase("获取进行中活动").with_variables(**({"type": "2"})).call(selUpwardActivityInfo).export(*["id", "actName"])),
        Step(RunTestCase("获取已结束活动").with_variables(**({"type": "3"})).call(selUpwardActivityInfo).export(*["id", "actName"])),

    ]

if __name__ == "__main__":
    Test_Circle_Dynamicst().test_start()



