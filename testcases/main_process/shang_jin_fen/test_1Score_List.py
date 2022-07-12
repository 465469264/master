#上级分页面
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.advLevelList import advLevelList
from api.app.usGrowthRights import usGrowthRights
from api.app.stdLearnInfo import stdLearnInfo
from api.app.gsAwardInfos import gsAwardInfos
from api.app.gsRuleInfos import gsRuleInfos
class Test_Score_List(HttpRunner):
    config = (
        Config("圈子页查看报名中-进行中-已结束")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "pageSize": 10,
                            "pageNum": 1,
                            "minLevel": "1",  # 显示的最低范围
                            "maxLevel": "8",  # 显示的最高范围
                            "advLevel": "1",

                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("返回所有上进分任务的情况").call(gsRuleInfos)),
        Step(RunTestCase("获取learnId").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("上进分-成长轨迹的等级列表").call(advLevelList)),
        Step(RunTestCase("上进分-成长权益").with_variables(**({"name":"勋章"})).call(usGrowthRights)),
        Step(RunTestCase("上进分-type传空").with_variables(**({"type": ""})).call(gsAwardInfos)),
        Step(RunTestCase("上进分-成长新人礼").with_variables(**({"type": "1"})).call(gsAwardInfos)),
        Step(RunTestCase("上进分-每日奖励").with_variables(**({"type": "2"})).call(gsAwardInfos)),
        Step(RunTestCase("上进分-学习奖励").with_variables(**({"type": "3"})).call(gsAwardInfos)),
        Step(RunTestCase("上进分-成长奖励").with_variables(**({"type": "4"})).call(gsAwardInfos)),

    ]

if __name__ == "__main__":
    Test_Score_List().test_start()



