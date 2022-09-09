from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.selLiveBroadcastPlanInfos import selLiveBroadcastPlanInfos
from api.app.liveInfos import liveInfos
from api.app.userHome import get_info
from api.app.instance import instance
from api.app.sendMsg import sendMsg_teacher
from api.app.selMessageList import selMessageList


#讲师在直播计划中-----进入直播
class Test_teacher_live(HttpRunner):
    config = (
        Config("讲师开播")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "msgType": "1",
                            "sourceType": "2",
                        }
                       )
                )
    teststeps = [
        Step(RunTestCase("获取账号信息").setup_hook('${Modify_lives_schedule(324)}').call(get_info).export(*["userId","realName"])),
        Step(RunTestCase("讲师获取直播计划").setup_hook('${delay(1)}').call(selLiveBroadcastPlanInfos).export(*["channelNum","id"])),
        Step(RunTestCase("获取直播间信息").with_variables(**({"groupId": "$channelNum"})).call(liveInfos)),
        Step(RunTestCase("建立消息通道，获取ip").call(instance)),
        Step(RunTestCase("讲师进入直播间--获取直播间弹幕").with_variables(**({"groupId": "$channelNum", "sort": "2"})).call(selMessageList)),
        Step(RunTestCase("管理员进入直播间--发送进入直播间").with_variables(**({"msgType": "1", "groupId": "$channelNum","cmd":"3", "userName": "$realName"})).call(sendMsg_teacher)),

                 ]

if __name__ == '__main__':
    Test_teacher_live().test_start()