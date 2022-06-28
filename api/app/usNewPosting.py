from httprunner import HttpRunner, Config, Step, RunRequest
#发布动态
class usNewPosting(HttpRunner):
    config = (
        Config("发布动态")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                            "scText": "$scText",
                                            "scType": "$scType",          #读书社:scType.2,  跑团：scType.3，  自考圈：scType.4	，同学圈：scType.1   ，职场圈：scType.5
                                            "subType": "$subType",           #普通贴：subType :0     1：读书贴  2：跑步贴）
                                            "scVideoUrl": "",
                                            "picUrlsImgWH": "{\"$scPicUrl\":{\"w\":918,\"h\":1357}}",
                                            "learnId": "$learnId",
                                            "scPicUrl": "$scPicUrl"
                                        },
                                        "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("发布普通帖子")
                .post("/proxy/us/usNewPosting/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "${ENV(app_auth_token)}",

            }
            )
                .with_data('$data')
                .validate()
                .assert_equal("body.message", "success")
        )
    ]
if __name__ == '__main__':
    usNewPosting().test_start()


