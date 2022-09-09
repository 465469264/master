from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.newUsLivesScheduleInfos import newUsLivesScheduleInfos
from api.app.liveInfos import liveInfos
from api.app.selMessageList import selMessageList
from api.app.sendMsg import sendMsg,send_message_usFollowNew
from api.app.usFollowNew import usFollowNew
from api.app.userHome import get_info
from api.app.selWatchRecord import selWatchRecord



from api.app.getLivesScheduleTeacherInfo import getLivesScheduleTeacherInfo
class Test_audience_live(HttpRunner):
    config = (
        Config("管理员接口")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "msgType": "1",
                            "sourceType": "2",  # 打赏来源类型 1: 课程 2: 直播广场

                        }
                       )
                )
    teststeps = [
        #管理员-获取直播广场-发送弹幕-点赞-关注-取消关注-全部禁言-解除禁言-单个禁言-解除禁言
        Step(RunTestCase("获取账号信息").setup_hook('${Modify_lives_schedule(324)}').call(get_info).export(*["realName","userId"])),
        Step(RunTestCase("app-获取直播计划").with_variables(**({"tab": "1"})).call(newUsLivesScheduleInfos).export(*["channelNum","id","name","liveAdminUserId"])),
        Step(RunTestCase("获取直播间信息").with_variables(**({"groupId": "$channelNum"})).call(liveInfos)),
        Step(RunTestCase("管理员进入直播间--获取直播间弹幕").with_variables(**({"groupId": "$channelNum","sort": "2"})).call(selMessageList)),
        Step(RunTestCase("直播间-管理员-群聊直播间-发送弹幕").with_variables(**({"groupId":"$channelNum","msgType": "1","cmd": "5","userName": "$realName","userIdentity": "2","content": "测试amylee"})).call(sendMsg)),
        Step(RunTestCase("获取讲师信息").with_variables(**({"liveId":"$id"})).call(getLivesScheduleTeacherInfo).export(*["teacher_userId","teacher_userName"])),
        Step(RunTestCase("直播间-关注讲师").with_variables(**({"operateType": "1","targetUserId": "$teacher_userId"})).call(usFollowNew)),
        Step(RunTestCase("关注讲师-发送弹幕").with_variables(**({"groupId": "$channelNum", "msgType": "1", "cmd": "10", "userName": "$realName", "userIdentity": "1","teacherName":"teacher_userName","teacherId":"teacher_userId"})).call(send_message_usFollowNew)),
        Step(RunTestCase("直播间-取消关注讲师").with_variables(**({"operateType": "2", "targetUserId": "$teacher_userId"})).call(usFollowNew)),
        Step(RunTestCase("管理员获取全部观众").with_variables(**({"groupId": "$channelNum"})).call(selWatchRecord)),



    ]

if __name__ == '__main__':
    Test_audience_live().test_start()