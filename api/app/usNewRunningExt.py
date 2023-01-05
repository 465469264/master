#这期的需求-APP短视频优化-----使用新的接口来发上进跑视频/跑步视频
from httprunner import HttpRunner, Config, Step, RunRequest
class usNewRunningExt(HttpRunner):
    config = (
        Config("跑步新接口")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "cycleType": "0",                        #0>没有习惯打卡  打卡周期类型 1: 连续 2：累计
                                            "sign": "7338E312D38F5F245E3BACDA3EF965BC",
                                            "runJson": "{\"runImg\":\"20221122053711587-9160.jpg\",\"distance\":\"3\",\"spendDesc\":\"6'20\\\"\",\"runSecond\":\"0.32\",\"identifier\":\"26BA6444-3233-45C0-B043-6853E0F62933\\/L0\\/001\",\"historyRun\":0,\"runTime\":\"00:19:00\"}",
                                            "scPicUrl": "",
                                            "subType": "2",
                                            "mappingIdType": "3",
                                            "scType": "3",
                                            "ifRunRecord": "1",
                                            "scVideoUrl": "",
                                            "scText": "11月累计第1天跑步"
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
            RunRequest("发帖新接口")
                .post("/proxy/us/usNewRunningExt/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]