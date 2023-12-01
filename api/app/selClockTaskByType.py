#活动页-根据类型进入跑步/读书/其他
from httprunner import HttpRunner, Config, Step, RunRequest
class selClockTaskByType(HttpRunner):
    config = (
        Config("#活动页-根据类型进入跑步/读书/其他")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                            "pageNum": "$pageNum",
                                            "pageSize": "$pageSize",
                                            "type": "$type",            # 2>读书打卡   3>跑步打卡  4>其他打卡
                                            "newVersion": "1",

    },
                                    "header": {"appType": "${ENV(appType)}"}
                           },
                            "data": "${base64_encode($number)}"
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("#活动页-根据类型进入跑步/读书/其他")
                .post("/proxy/mkt/selClockTaskByType/1.0/")
                .with_headers(**{
                                    "User-Agent": "${ENV(User-Agent)}",
                                    "Content-Type": "text/yzedu+; charset=UTF-8",
                                    "Host": "${ENV(app_Host)}",
                                    "authtoken": "${ENV(app_auth_token)}",
                                    }
                              )
                .with_data('$data')
                .extract()
                .with_jmespath("body.body", "body")
                .validate()
                .assert_equal("body.message", "$message")

        )
    ]

if __name__ == '__main__':
    selClockTaskByType().test_start()