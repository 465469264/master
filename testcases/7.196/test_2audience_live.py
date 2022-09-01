from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.newUsLivesScheduleInfos import newUsLivesScheduleInfos
from api.app.sendMsg import sendMsg,send_message_gift,send_message_usFollowNew
from api.app.usFollowNew import usFollowNew
from api.app.livePraise import livePraise
from api.app.stdLearnInfo import stdLearnInfo
from api.app.usRewardGift import usRewardGift
from  api.app.selLiveGift import selLiveGift
from api.web.zhimi_give_toAdd_do import zhimi_token
from api.app.userHome import get_info
from api.web.zhimi_give_add_do import zhimi_give
from api.web.zhimi_give_check_list_do import zhimi_give_check_list
from api.web.zhimi_give_check_toCheck_do import zhimi_check_token
from api.web.zhimi_give_check_check_do import check_zhimi

from api.app.getLivesScheduleTeacherInfo import getLivesScheduleTeacherInfo
class Test_audience_live(HttpRunner):
    config = (
        Config("直播列表")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "msgType": "1",
                            "sourceType": "2",  # 打赏来源类型 1: 课程 2: 直播广场
                            "giftType": "1",
                            #赠送智米参数
                            "mobile": "${read_data_number(ApplyRecord,mobile)}",
                            "accType": "2",  # accType.1	>现金账户	 2>智米	 3>滞留账户
                            "pageSize": "20",
                            "pageNum": "1",
                            "amount": "100",  # 100智米
                            "a": "1",
                            "zhimiType": "1",  # 1>进账   2>出账
                            "reasonStatus": "2",  # 2>通过   3>驳回
                        }
                       )
                )
    teststeps = [
        # 智米赠送申请
        Step(RunTestCase("取智米赠送的web_token").setup_hook('${login_web()}', "Cookie").call(zhimi_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token", "Cookie"])),
        Step(RunTestCase("获取用户信息，获取userId").setup_hook('${delay(1)}').call(get_info).export(*["userId"])),
        Step(RunTestCase("后台申请智米赠送100").with_variables(**({"zhimiCount": "$amount", "accSerialType": "5", })).call(zhimi_give)),
        # 智米赠送审核
        Step(RunTestCase("获取要审核的记录id").setup_hook('${delay(1)}').call(zhimi_give_check_list).export(*["id"])),
        Step(RunTestCase("获取智米审核web_token").call(zhimi_check_token).teardown_hook('${get_html($body)}',"_web_token").export(*["_web_token"])),
        Step(RunTestCase("智米赠送").call(check_zhimi)),
        #获取直播广场-发送弹幕-点赞-关注-取消关注-赠送智米-赠送智米发送弹幕-离开直播间
        Step(RunTestCase("获取账号信息").setup_hook('${Modify_lives_schedule(324)}', "").call(get_info).export(*["realName","userId"])),
        Step(RunTestCase("app-获取直播计划").with_variables(**({"tab": "1"})).call(newUsLivesScheduleInfos).export(*["channelNum","id","name","liveAdminUserId"])),
        Step(RunTestCase("直播间-观众-群聊直播间-发送弹幕").with_variables(**({"groupId":"$channelNum","msgType": "1","cmd": "5","userName": "$realName","userIdentity": "1","content": "测试amylee"})).call(sendMsg)),
        Step(RunTestCase("获取讲师信息").with_variables(**({"liveId":"$id"})).call(getLivesScheduleTeacherInfo).export(*["teacher_userId","teacher_userName"])),
        Step(RunTestCase("直播间-关注讲师").with_variables(**({"operateType": "1","targetUserId": "$teacher_userId"})).call(usFollowNew)),
        Step(RunTestCase("关注讲师-发送弹幕").with_variables(**({"groupId": "$channelNum", "msgType": "1", "cmd": "10", "userName": "$realName", "userIdentity": "1","teacherName":"teacher_userName","teacherId":"teacher_userId"})).call(send_message_usFollowNew)),
        Step(RunTestCase("直播间-取消关注讲师").with_variables(**({"operateType": "2", "targetUserId": "$teacher_userId"})).call(usFollowNew)),
        # Step(RunTestCase("直播间点赞").with_variables(**({"groupId": "$channelNum"})).call(livePraise)),
        Step(RunTestCase("获取用户的stdid").call(stdLearnInfo).export(*["stdId"])),
        Step(RunTestCase("获取直播间的礼物赠送配置").call(selLiveGift).export(*["money","gift_name","giftType"])),
        Step(RunTestCase("直播间赠送智米").with_variables(**({"mappingId": "$id","giftName": "$gift_name","teaEmpName": "$teacher_userName","stuLearnId": "$stdId","teaEmpId": "$teacher_userId","stuUserName": "$realName","courseTimeName": "$name","type": "5"})).call(usRewardGift)),
        Step(RunTestCase("赠送智米后发送智米弹幕").with_variables(**({"mappingId": "$id","groupId": "$channelNum", "msgType": "1", "cmd": "11", "userName": "$realName", "userIdentity": "1","giftName": "$gift_name","teaEmpName": "$teacher_userName","teaEmpId": "$teacher_userId","stuUserName": "$realName","courseTimeName": "$name","type": "5","content": ""})).call(send_message_gift)),
        Step(RunTestCase("观众了离开直播间-发至管理员").with_variables(**({"groupId":"$channelNum","msgType": "2","cmd": "4","receiverId":"$liveAdminUserId","userName": "$realName","userIdentity": "1","content": ""})).call(sendMsg)),

    ]

if __name__ == '__main__':
    Test_audience_live().test_start()