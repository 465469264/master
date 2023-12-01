#读书笔记发帖
from httprunner import HttpRunner, Config, Step, RunRequest

class UsNewReadExt(HttpRunner):
    config = (
        Config("读书笔记发帖")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                        "body":{
                                                "timeStamp": "${timestap()}",
                                                "cycleType": "$cycleType",        #无：0  打卡周期类型 1: 连续 2：累计
                                                "scPicUrl": "",
                                                "mappingId": "$mappingId",        #书籍id
                                                "subType": "$subType",                 #帖子二级类型（1：读书贴  2：跑步贴）
                                                "scSource": "2",
                                                "scType": "$scType",                    #圈子类型    0  => 首页 1  => 同学圈 2  => 读书会 3  => 跑团圈 4  => 自考圈
                                                "scVideoUrl": "",
                                                "extContent": "{\"bookUrl\":\"$imgUrl\",\"readPersonNum\":$readPersonNum,\"bookName\":\"$name\"}",
                                                "scText": "$scText"

                                        },
                                        "header": {"appType": "${ENV(appType)}"}
                                        },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("读书笔记发帖")
                .post("/proxy/us/usNewReadExt/1.0/")
                .with_headers(**{
                                "User-Agent": "${ENV(User-Agent)}",
                                "Content-Type": "text/yzedu+; charset=UTF-8",
                                "Host": "${ENV(app_Host)}",
                                "authtoken": "${ENV(app_auth_token)}",
                            }
                              )
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
