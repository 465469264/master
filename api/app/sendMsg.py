from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
#观看端-直播间发送消息
class sendMsg(HttpRunner):
    config = (
        Config("直播间发送消息")
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
                    "Host":"${ENV(im_host)}",
                    "Connection":"Keep-Alive"
                }
            )
            .with_json({
                        "userId": "$userId",
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

#赠送智米--发送弹幕
class send_message_gift(HttpRunner):
    config = (
        Config("直播间-赠送智米发送消息")
            .base_url("${ENV(im)}")
            .verify(False)
            .variables(**{
        }
                       )
    )
    teststeps = [
        Step(
            RunRequest("直播间-赠送智米发送消息")
            .post("/proxy/sendMsg/1.0/")
            .with_headers(
                        **{
                        "User-Agent": "yuan zhi jiao yu/7.19.6 (iPhone; iOS 12.5.5; Scale/3.00)",
                        "Content-Type": "application/json",
                        "Host": "${ENV(im_host)}",
                        "Connection": "Keep-Alive"
                            }
                        )
            .with_json({
                        "platform": "iOS",
                        "msgType": "$msgType",                                #1:群聊 2：私聊
                        "content": "$content",
                        "appType": "4",
                        "userIdentity": "$userIdentity",                     # 用户身份 1：普通用户 2：管理员
                        "groupId": "$groupId",
                        "userName": "$userName",                             #赠送人的userName
                        "extParam": "{\"teaEmpId\":\"$teaEmpId\",\"giftName\":\"$giftName\",\"giftType\":\"$giftType\",\"sourceType\":\"$sourceType\",\"courseTimeName\":\"$courseTimeName\",\"teaEmpName\":\"$teaEmpName\",\"stuUserName\":\"$stuUserName\",\"mappingId\":\"$mappingId\",\"stuLearnId\":\"\",\"type\":\"$type\",\"money\":\"$money\"}",
                        "userId": "$userId",                                 #赠送人的userId
                        "cmd": "$cmd",  # cmd：1绑定 2心跳 3上线 4下线 5 写 6异常 7禁言 8：开言 9：点赞 10：关注 11：打赏 12:主播关闭 13：回来后开启
                        "headImg": ""
                        })
            .extract()
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]

#观众离开直播间，发送信息至管理员
class live_sendMsg(HttpRunner):
    config = (
        Config("观众离开直播间，发送信息至管理员")
            .base_url("${ENV(im)}")
            .verify(False)
            .variables(**{
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("观众离开直播间，发送信息至管理员")
            .post("/proxy/sendMsg/1.0/")
            .with_headers(
                **{
                    "User-Agent": "yuan zhi jiao yu/7.19.6 (iPhone; iOS 12.5.5; Scale/3.00)",
                    "Content-Type": "application/json",
                    "Host":"${ENV(im_host)}",
                    "Connection":"Keep-Alive"
                }
            )
            .with_json({
                        "userId": "$userId",
                        "userName": "$userName",
                        "receiverId": "164636031060872217",                     #管理员userId
                        "cmd": "$cmd",                                           #cmd：1绑定 2心跳 3上线 4下线 5 写 6异常 7禁言 8：开言 9：点赞 10：关注 11：打赏 12:主播关闭 13：回来后开启
                        "userIdentity": "$userIdentity",                        #用户身份 1：普通用户 2：管理员
                        "appType": "4",                                         #3>安卓   4>ios
                        "platform": "iOS",                                      #端
                        "msgType": "$msgType",                                   #1:群聊 2：私聊
                        "groupId": "$groupId",                                  #用户房间组 msgType=1为必传
                        "content": "$content"                               #弹幕内容
                    })
            .extract()
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]

#用户关注主讲人发送弹幕
class send_message_usFollowNew(HttpRunner):
    config = (
        Config("用户关注主讲人发送弹幕")
            .base_url("${ENV(im)}")
            .verify(False)
            .variables(**{
        }
                       )
    )
    teststeps = [
        Step(
            RunRequest("用户关注主讲人发送弹幕")
            .post("/proxy/sendMsg/1.0/")
            .with_headers(
                        **{
                        "User-Agent": "yuan zhi jiao yu/7.19.6 (iPhone; iOS 12.5.5; Scale/3.00)",
                        "Content-Type": "application/json",
                        "Host": "${ENV(im_host)}",
                        "Connection": "Keep-Alive"
                            }
                        )
            .with_json({
                        "platform": "iOS",
                        "msgType": "$msgType",                                #1:群聊 2：私聊
                        "content": "关注了主讲人",
                        "appType": "4",
                        "userIdentity": "$userIdentity",                     # 用户身份 1：普通用户 2：管理员
                        "groupId": "$groupId",
                        "userName": "$userName",                             #赠送人的userName
                        "extParam": "{\"teacherName\":\"$teacherName\",\"teacherHeadUrl\":\"livesHeadImg\\\",\"teacherId\":\"$teacherId\"}",
                        "userId": "$userId",                                 #赠送人的userId
                        "cmd": "$cmd",                                       # cmd：1绑定 2心跳 3上线 4下线 5 写 6异常 7禁言 8：开言 9：点赞 10：关注 11：打赏 12:主播关闭 13：回来后开启
                        "headImg": ""
                        })
            .extract()
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]


#讲师进入直播间-发送进入直播间弹幕
class sendMsg_teacher(HttpRunner):
    config = (
        Config("讲师进入直播间-发送进入直播间弹幕")
            .base_url("${ENV(im)}")
            .verify(False)
            .variables(**{
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("讲师进入直播间-发送进入直播间弹幕")
            .post("/proxy/sendMsg/1.0/")
            .with_headers(
                **{
                    "User-Agent": "yuan zhi jiao yu/7.19.6 (iPhone; iOS 12.5.5; Scale/3.00)",
                    "Content-Type": "application/json",
                    "Host":"${ENV(im_host)}",
                    "Connection":"Keep-Alive"
                }
            )
            .with_json({
                            "platform": "iOS",
                            "userIdentity": "1",
                            "extParam": "{\"isForbid\":\"7\"}",
                            "appType": "4",
                            "content": "进入了直播间",
                            "msgType": "$msgType",                                                        #1:群聊 2：私聊
                            "userId": "$userId",
                            "userName": "$userName",
                            "groupId": "$groupId",
                            "cmd": "$cmd",                                                            #cmd：1绑定 2心跳 3上线 4下线 5 写 6异常 7禁言 8：开言 9：点赞 10：关注 11：打赏 12:主播关闭 13：回来后开启
                            "headImg": "",
                        })
            .extract()
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]