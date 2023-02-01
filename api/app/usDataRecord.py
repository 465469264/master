#用户数据埋点
from httprunner import HttpRunner, Config, Step, RunRequest
class usDataRecord(HttpRunner):
    config = (
        Config("用户数据埋点")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                                "unit": "$unit",                       #单位 : 1/次数 2/分钟 3/秒
                                                "onlineDuration": "$onlineDuration",             #时长
                                                "eventType": "$eventType",                  #eventType   1：下载 2：视频时长
                                                "businessType": "$businessType",               #：课程资料 2：复习资料 3：直播 4：录播 5：回放 6：短视频 7：直播广场直播 8：直播广场录播 9：直播广场回放
                                                # "learnId": "$learnId",
                                                "mappingId": "$mappingId"
                                        },
                                    "header":{
                                            "appType": "3",
                                        }
                                },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("用户数据埋点")
                .post("/proxy/us/usDataRecord/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}"}
                              )
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]