#我的活动的接口
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.selMyUpwardActivityInfo import selMyUpwardActivityInfo


class Test_Circle_Dynamicst(HttpRunner):
    config = (
        Config("圈子页查看报名中-进行中-已结束")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "pageSize": 10,
                            "pageNum": 1

                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("圈子页查看活动页-报名中").with_variables(**({"type":1})).call(selMyUpwardActivityInfo)),
        Step(RunTestCase("圈子页查看活动页-进行中").with_variables(**({"type": 2})).call(selMyUpwardActivityInfo)),
        Step(RunTestCase("圈子页查看活动页-已结束").with_variables(**({"type": 3})).call(selMyUpwardActivityInfo)),

    ]

if __name__ == "__main__":
    Test_Circle_Dynamicst().test_start()



