#上进分-成长权益模块
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.gsMedalInfos import gsMedalInfos
from api.app.gsLevelRewardInfos import gsLevelRewardInfos
from api.app.gsReceiveLevelZhimi import gsReceiveLevelZhimi


class Test_GrowthRights(HttpRunner):
    config = (
        Config("上进分-成长权益模块")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "type": "2"
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("成长权益-我的勋章").call(gsMedalInfos)),
        Step(RunTestCase("成长权益-智米奖励").call(gsLevelRewardInfos).teardown_hook('${ifReceive($ifReceive)}',"message1").export(*["id"],"message1")),
        Step(RunTestCase("智米奖励-领取智米").with_variables(**({"levelInfoId":"$id","message":"$message1"})).call(gsReceiveLevelZhimi)),


    ]

if __name__ == "__main__":
    Test_GrowthRights().test_start()



