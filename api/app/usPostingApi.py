#2022年11月的APP短视频优化版本后使用的新发帖接口          0>关注  1>同学圈  2>读书社  3>跑团  4>自考圈
from httprunner import HttpRunner, Config, Step, RunRequest
class usPostingApi(HttpRunner):
    config = (
        Config("发帖新接口")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                        "scText": "$scText",
                                        "scType": "$scType",               #0>关注  1>同学圈  2>读书社  3>跑团  4>自考圈
                                        "subType": "$subType",              #普通贴：subType :0     1：读书贴  2：跑步贴）
                                        "scPicUrl": "$scPicUrl",
                                        "scVideoUrl": "",
                                        "learnId": "$learnId",
                                        "scSource": "$scSource"                 #帖子来源，1.安卓，2.iOS 3. 公众号 4.上进学社 5.红包
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
                .post("/proxy/us/usPostingApi/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].id", "id")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]