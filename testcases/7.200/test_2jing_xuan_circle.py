#这期的需求--增加一个精选的圈子列表，取所有过往的热门帖子在这（不包含现在的热门帖子）   "dictName" : "精选", "dictValue" : "-1","dictName" : "最新",  "dictValue" : null,
from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.getDictSettings import getDictSettings
from api.app.selCircleDynamicInfos import selCircleDynamicInfos5

class Test_jing_xian_circle(HttpRunner):
    config = (
        Config("查看精选圈子")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "pageSize": "20",
                            "userRoleType": 2,
                            "pageNum": 1,
                            "own": "0"
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取圈子列表").call(getDictSettings)),
        Step(RunTestCase("查看精选圈子").with_variables(**({"scType": "-1"})).call(selCircleDynamicInfos5)),

    ]
if __name__ == '__main__':
    Test_jing_xian_circle().test_start()