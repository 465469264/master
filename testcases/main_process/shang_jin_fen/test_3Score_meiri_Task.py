#做上进分每日奖励任务
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.stdLearnInfo import stdLearnInfo
from api.app.gsAwardInfos import gsAwardInfos2
from api.app.gsOnlineRecord import gsOnlineRecord
from api.app.gsOnlineRecord import gsOnlineRecord2


class Test_Score_meiri_Task(HttpRunner):
    config = (
        Config("上进分-每日奖励做任务")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "type": "2",
                            "unit": "1"
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取learnId").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("上进分-判断“每日登录APP一次”任务已完成").with_variables(**({"a":"0","sort":1})).call(gsAwardInfos2).export(*["id0","ruleCode0","ruleGroup0","rewardType","ruleGroup","ruleCode1","id1","ruleCode2","id2","ruleCode3","id3","ruleCode4","id4"])),
        Step(RunTestCase("做每日登录APP一次触发").with_variables(**({"ruleCode":"$ruleCode0","id":"$id0","ruleGroup": "ruleGroup0"})).call(gsOnlineRecord2)),
        Step(RunTestCase("做在线30分钟任务触发").with_variables(**({"time": "1","ruleCode":"$ruleCode1","id":"$id1"})).call(gsOnlineRecord)),
        Step(RunTestCase("做在线60分钟任务触发").with_variables(**({"time": "2","ruleCode":"$ruleCode2","id":"$id2"})).call(gsOnlineRecord)),
        Step(RunTestCase("做在线120分钟任务触发").with_variables(**({"time": "3", "ruleCode":"$ruleCode3","id": "$id3"})).call(gsOnlineRecord)),
        Step(RunTestCase("做在线240分钟任务触发").with_variables(**({"time": "4", "ruleCode": "$ruleCode4","id": "$id4"})).call(gsOnlineRecord)),

    ]

if __name__ == "__main__":
    Test_Score_meiri_Task().test_start()



