from httprunner import HttpRunner, Config, Step, RunRequest
#修改圈子的branner
class circleDynamic_bannerEdit(HttpRunner):
    config = (
        Config("修改圈子的branner")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("获取修改branner的 webtoken")
                .post("/circleDynamic/bannerEdit.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Host": "${ENV(Host)}",
                "Cookie":"$Cookie"
            })
                .with_data({
                            "_web_token": "$_web_token",
                            "exType": "UPDATE",
                            "bannerId": "$bannerId",
                            "historyNum": "$historyNum",
                            "appBannerType": "$appBannerType",
                            "sort": "$sort",
                            "bannerPic":"",
                            "bannerUrl": "$bannerUrl",
                            "isPhotoChange":"",
                            "bannerName": "$bannerName",
                            "bannerDesc": "$bannerDesc",
                            "bannerType": "2",
                            "mappingId":"",
                            "isAllow": "1",
            })
                .extract()
                .with_jmespath("body","body")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]