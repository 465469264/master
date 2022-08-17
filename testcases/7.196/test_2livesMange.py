from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.web.livesManage_list import livesManage_list
from api.app.newUsLivesScheduleInfos import newUsLivesScheduleInfos
from api.app.userHome import get_info
from api.app.sendMsg import sendMsg
from api.app.livePraise import livePraise

class Test_lives_admin(HttpRunner):
    config = (
        Config("直播列表")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "msgType": "1",
                            "content": "测试amylee"
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取账号信息").call(get_info).export(*["realName","userId"])),
        Step(RunTestCase("app-获取直播广场").call(newUsLivesScheduleInfos).export(*["channelNum"])),
        Step(RunTestCase("直播间-群聊直播间发送弹幕").with_variables(**({"groupId":"$channelNum","msgType": "1","cmd": "5","userName": "$realName","userIdentity": "1"})).call(sendMsg)),
        Step(RunTestCase("直播间-点赞讲师").with_variables(**({"groupId":"$channelNum"})).call(livePraise)),

    ]

if __name__ == '__main__':
    Test_lives_admin().test_start()