from httprunner import HttpRunner, Config, Step, RunRequest
# 读书打卡发帖
class usReadExt(HttpRunner):
    config = (
        Config("读书打卡发帖")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                    "cycleType": "$cycleType",                  #打卡周期类型 1: 连续 2：累计
                                    "mappingId": "$bookId",
                                    "learnId": "$learnId",
                                    "taskEnrollId": "$taskEnrollId",            #任务报名id
                                    "scPicUrl": "",
                                    "subType": "$subType",                              #普通贴：subType :0     1：读书贴  2：跑步贴）
                                    "markTaskType": "$markTaskType",                           #任务打卡类型：2：读书  3：跑步    4：其他
                                    "iOS_version": "7.19.4",
                                    "scType": "$scType",                                    #读书社:scType.2,  跑团：scType.3，  自考圈：scType.4	，同学圈：scType.1   ，职场圈：scType.5
                                    "scVideoUrl": "",
                                    "taskId": "$taskId",
                                    "extContent": "{\"bookUrl\":\"$imgUrl\",\"readPersonNum\":$readPersonNum,\"bookName\":\"$name\"}",
                                    "scText": "$topicName"+"$markContent"
                                },
                                    "header":{"appType":"3"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("带出书籍")
                .post("/proxy/us/usReadExt/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "success")


        )
    ]

if __name__ == '__main__':
    usReadExt().test_start()