#圈子页-读书
from httprunner import HttpRunner, Config, Step, RunRequest
class selCommonlyUsedBooks(HttpRunner):
    config = (
        Config("圈子页-读书")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "userId": "$userId",
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
            RunRequest("圈子页-读过的读书")
                .post("/proxy/us/selCommonlyUsedBooks/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",

                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].bookId","bookId")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]