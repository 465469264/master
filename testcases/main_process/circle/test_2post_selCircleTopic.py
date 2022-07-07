#发帖带话题词
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.selCircleTopic import selCircleTopic
from api.app.stdLearnInfo import stdLearnInfo
from api.app.userHome import get_info
from api.app.usNewPosting import usNewPosting
from api.app.selCircleDynamicInfos import selCircleDynamicInfos2
from api.app.usSetDynamics import usSetDynamics


class post_selCircleTopic(HttpRunner):
    config = (
        Config("习惯打卡里的接口")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "pageSize": "10",
                            "pageNum": "1",
                            "type": "0",              #返回所有话题
                            "subType": "0",           #普通帖子
                            "own": "1",
                            "userRoleType": "",
                            "status": "3",  # 3>删除

                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("返回话题").call(selCircleTopic).export(*["topicName"])),
        Step(RunTestCase("获取登陆人参数").call(get_info).export(*["userId1"])),
        Step(RunTestCase('获取用户报读信息').call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase('发布帖子带图片至读书社').with_variables(**({"scType": "2", "scPicUrl": "", "scText": "#$topicName#"+"自动发帖"})).call(usNewPosting)),
        Step(RunTestCase("进入自己的主页").call(selCircleDynamicInfos2).export(*["id"])),
        Step(RunTestCase("删除自己的第一条圈子").with_variables(**({"circleUserId": "$userId"})).call(usSetDynamics)),

    ]

if __name__ == "__main__":
    post_selCircleTopic().test_start()



