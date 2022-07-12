#根据课程id,查询课程的有效时间
from httprunner import HttpRunner, Config, Step, RunRequest
class selCourseTimeById(HttpRunner):
    config = (
        Config("我的课表-返回课程名称")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "learnId": "$learnId",
                                            "type": "1",
                                            "courseId": "$courseId",               #课程id,不传时返回所有
                                            "stageId": ""                 #阶段，不传时查询所有

                                    },
                                    "header":{
                                            "appType":"3"
                                            }
                                    },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("我的课表-返回课程名称")
                .post("/proxy/bds/selCourseTimeById/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].details[0].courseId","courseId")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
