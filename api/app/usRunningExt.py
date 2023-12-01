from httprunner import HttpRunner, Config, Step, RunRequest
#上进跑
class usNewRunningExt(HttpRunner):
    config = (
        Config("上进跑发帖")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                                "cycleType": "0",                               #打卡周期类型 1: 连续 2：累计
                                                "runJson": "{\"runImg\":\"$scPicUrl\",\"stepFrequency\":\"$stepFrequency\",\"fastSpendDesc\":\"$fastSpendDesc\\\"\",\"runSecond\":\"$runSecond\",\"totalSteps\":\"$totalSteps\",\"spendDesc\":\"$spendDesc\\\"\",\"slowSpendDesc\":\"$slowSpendDesc\\\"\",\"distance\":\"$distance\",\"trackFileUrl\":\"20231130033618983-483.txt\",\"runTime\":\"$runTime\"}",
                                                "timeStamp": "${timestap()}",
                                                "scPicUrl": "",                                #图片路径，除轨迹图的发图
                                                "subType": "$subType",
                                                "runRecordId": "$runRecordId",                #跑步记录id
                                                "mappingIdType": "$mappingIdType",            #任务打卡类型：2：读书  3：跑步    4：其他
                                                "scType": "$scType",                      #圈子  0>关注  1>同学圈  2>读书社  3>跑团  4>自考圈
                                                "ifRunRecord": "$ifRunRecord",     #是否生成跑步记录  1：是（发帖+跑步记录）  0：否（单纯发跑步帖子
                                                "scVideoUrl": "",                   #视频
                                                "scSource": "$scSource",
                                                "scText": "$scText"
                                        },
                                        "header":{"appType":"${ENV(appType)}"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("上进跑打卡")
                .post("/proxy/us/usNewRunningExt/1.0/")
                .with_headers(**{
                                    "User-Agent": "${ENV(User-Agent)}",
                                    "Content-Type": "text/yzedu+; charset=UTF-8",
                                    "Host": "${ENV(app_Host)}",
                                    "authtoken": "${ENV(app_auth_token)}",
                                }
            )
                .with_data('$data')
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]



from httprunner import HttpRunner, Config, Step, RunRequest
#上进跑
class usNewRunningExt_Uplod(HttpRunner):
    config = (
        Config("跑步上传图片")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                                "cycleType": "0",                               #打卡周期类型 1: 连续 2：累计
                                                "runJson": "{\"runImg\":\"$scPicUrl\",\"distance\":\"$distance\",\"spendDesc\":\"$spendDesc\\\"\",\"runSecond\":\"$runSecond\",\"identifier\":\"E96F0803-6534-401B-9716-8CDC16946FD1\\/L0\\/001\",\"historyRun\":$historyRun,\"runTime\":\"$runTime\"}",
                                                "timeStamp": "${timestap()}",
                                                "scPicUrl": "",                                #图片路径，除轨迹图的发图
                                                "subType": "$subType",
                                                "runRecordId": "$runRecordId",                #跑步记录id
                                                "mappingIdType": "$mappingIdType",            #任务打卡类型：2：读书  3：跑步    4：其他
                                                "scType": "$scType",                      #圈子  0>关注  1>同学圈  2>读书社  3>跑团  4>自考圈
                                                "ifRunRecord": "$ifRunRecord",     #是否生成跑步记录  1：是（发帖+跑步记录）  0：否（单纯发跑步帖子
                                                "scVideoUrl": "",                   #视频
                                                "scSource": "$scSource",
                                                "scText": "$scText"
                                        },
                                        "header":{"appType":"${ENV(appType)}"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("上进跑打卡")
                .post("/proxy/us/usNewRunningExt/1.0/")
                .with_headers(**{
                                    "User-Agent": "${ENV(User-Agent)}",
                                    "Content-Type": "text/yzedu+; charset=UTF-8",
                                    "Host": "${ENV(app_Host)}",
                                    "authtoken": "${ENV(app_auth_token)}",
                                }
            )
                .with_data('$data')
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]



