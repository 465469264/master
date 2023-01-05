from httprunner import HttpRunner, Config, Step, RunRequest
#点赞活动
class usNewRunningExt(HttpRunner):
    config = (
        Config("跑步任务打卡发帖")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                            "scText": "$topicName"+"$markContent",                              #习惯打卡术语
                                            "runJson": "{\"runImg\":\"$scPicUrl\",\"distance\":\"$distance\",\"spendDesc\":\"$spendDesc\\\"\",\"runSecond\":\"$runSecond\",\"runTime\":\"$runTime\"}",
                                            "userId": "$userId",
                                            "scSource": "$scSource",                                                    #帖子来源，1.安卓，2.iOS 3. 公众号 4.上进学社 5.红包
                                            "markTaskType": "$markTaskType",                                  #任务打卡类型：2：读书  3：跑步    4：其他
                                            "cycleType": "$cycleType",                                     #打卡周期类型 1: 连续 2：累计
                                            "taskEnrollId": "$taskEnrollId",                               #任务报名id
                                            "scType": "$scType",                                     #读书社:scType.2,  跑团：scType.3，  自考圈：scType.4	，同学圈：scType.1   ，职场圈：scType.5
                                            "learnId": "$learnId",
                                            "subType": "$subType",                                         #普通贴：subType :0     1：读书贴  2：跑步贴）
                                            "mappingIdType": "$mappingIdType",                        #外键mappingid类型（1：读书 2：自考课次 3：跑步）
                                            "taskId": "$taskId",                                    #习惯打卡id
                                             "ifRunRecord": "$ifRunRecord",                            # 是否生成跑步记录  1：是（发帖+跑步记录）  0：否（单纯发跑步帖子）
                                            "scPicUrl": "",

                                        },
                                        "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("跑步任务打卡")
                .post("/proxy/us/usNewRunningExt/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "text/yzedu+; charset=UTF-8",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "${ENV(app_auth_token)}",

            }
            )
                .with_data('$data')
                .validate()
                # .assert_equal("body.message", "success")
        )
    ]
if __name__ == '__main__':
    usNewRunningExt().test_start()


