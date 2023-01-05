from httprunner import HttpRunner, Config, Step, RunRequest
#APP获取个人信息
class zkStuServiceStatus(HttpRunner):
    config = (
        Config("登录后获取个人信息")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number":{
                                    "body": {
                                        "learnId": "$learnId",
                                    },
                                    "header": {
                                        "appType": "4",
                                    }
                                },
                          "data": "${base64_encode($number)}",
                          }
                       )
    )
    teststeps = [
        Step(
            RunRequest("获取个人信息")
                .post("/proxy/us/zkStuServiceStatus/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                "Content-Length": "308"
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.learnInfos[1].scholarship", "scholarship")
                .with_jmespath("body.body.learnInfos[1].learnId", "learnId")
                # 项目描述：
                # 远智教育是一家成人教育一站式上进学习平台公司，我负责的学员系统后台，
                # 以及远智教育app的测试。远志教育app，主要功能有，学员报名报读，上课，
                # 看课程直播，跑步，商城，支付等功能。我在项目中，独立负责整个项目的功
                # 能测试，以及接口自动化测试。其中最有挑战的是做其中的直播项目，有主播端，
                # 以及观看端。还有就跑步功能，用于给职工以及学员每天进行跑步公里数，配速打卡。
                #项目职责
                #1.负责学员系统的功能测试，数据流转
                #2.负责app的兼容测试，功能测试，稳定性测试
                #3.使用httprunner框架独立编写app和后台的接口自动化
                #4.协助运营人员解答学员的app使用问题
                #5.全程眼踪进度,把控产品质量:
                #6.进行bug的定位,协助开发修复bug,提高版本质量;
                #7.归纳并输出公司产品的主要业务逻辑

                .with_jmespath("body.body.learnInfos[1].unvsId", "unvsId")
                .with_jmespath("body.body.learnInfos[1].grade", "grade")
                .with_jmespath("body.body.learnInfos[1].unvsName", "unvsName")
                .with_jmespath("body.body.learnInfos[0].learnId", "learnId1")
                .with_jmespath("body.body.std_name", "std_name")
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]