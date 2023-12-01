#获取习惯打卡列表下的封面，参与人头像，参与人数
from httprunner import HttpRunner, Config, Step, RunRequest
class selClockTaskTabInfos(HttpRunner):
    config = (
        Config("获取习惯打卡列表下的参与人头像")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                            "type": "$type"            # 2>读书打卡   3>跑步打卡  4>其他打卡
                                            },
                                    "header": {"appType": "${ENV(appType)}"}
                                    },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("获取习惯打卡列表下的参与人头像")
                .post("/proxy/mkt/selClockTaskTabInfos/1.0/")
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

if __name__ == '__main__':
    selClockTaskTabInfos().test_start()