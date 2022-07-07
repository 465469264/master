#发帖@1个，@多个
from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.stdLearnInfo import stdLearnInfo
from api.app.userHome import get_info
from api.app.usFollowInfos import usFollowInfos
from api.app.usNewPosting import usNewPosting2
from api.app.selCircleDynamicInfos import selCircleDynamicInfos2
from api.app.usSetDynamics import usSetDynamics

class Test_Read_habbit(HttpRunner):
    config = (
        Config("发帖@")
            .verify(False)
            .variables(**{
                        "message": "success",
                        "subType": "0",                     #普通贴
                        "own": "1",                         #只看自己的发帖
                        "pageSize": 5,
                        "userRoleType": "",
                        "pageNum": 1,
                        "status": "3",  # 3>删除
                        "keyWord": "amylee"
                            }
                       )
             )
    teststeps = [
        Step(RunTestCase("获取登陆人参数").call(get_info).export(*["userId"])),
        Step(RunTestCase('获取用户报读信息').call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("查询需要@的人").call(usFollowInfos).export(*["realName","userId1"])),
        Step(RunTestCase('发布帖子@一个人').with_variables(**({"scType": "2","userName":"$realName","userId":"$userId1","scText": "@$realName"+"\b自动发帖艾特一个人测试"})).call(usNewPosting2)),
        Step(RunTestCase("进入自己的主页").call(selCircleDynamicInfos2).export(*["id"])),
        Step(RunTestCase("删除自己的第一条圈子").with_variables(**({"circleUserId": "$userId"})).call(usSetDynamics)),
    ]
if __name__ == '__main__':
    Test_Read_habbit().test_start()