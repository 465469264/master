from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
#直播间发送消息
class sendMsg(HttpRunner):
    config = (
        Config("获取直播广场列表")
            .base_url("${ENV(im)}")
            .verify(False)
            .variables(**{
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("直播间发送消息")
            .post("/proxy/sendMsg/1.0/")
            .with_headers(
                **{
                    "User-Agent": "yuan zhi jiao yu/7.19.6 (iPhone; iOS 12.5.5; Scale/3.00)",
                    "Content-Type": "application/json",
                    "Host":"27-im.yzwill.cn",
                    "Connection":"Keep-Alive"
                }
            )
            .with_json({
                        "userId": "$userId",
                        "timeStamp": 1658483952,
                        "deviceId": "4FE353FD-E0DF-431E-BC5E-5DA1F3AA9668",
                        "userName": "$userName",
                        "cmd": "$cmd",                                #cmd：1绑定 2心跳 3上线 4下线 5 写 6异常 7禁言 8：开言 9：点赞 10：关注 11：打赏 12:主播关闭 13：回来后开启
                        "userIdentity": "$userIdentity",                       #用户身份 1：普通用户 2：管理员
                        "appType": "4",                            #3>安卓   4>ios
                        "platform": "iOS",                         #端
                        "msgType": "$msgType",                            #1:群聊 2：私聊
                        "groupId": "$groupId",                     #用户房间组 msgType=1为必传
                        "content": "$content"                            #弹幕内容
                    })
            .extract()
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]


if __name__ == "__main__":
    sendMsg().test_start()