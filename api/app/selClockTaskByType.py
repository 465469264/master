#活动页-根据类型进入跑步/读书/其他
from httprunner import HttpRunner, Config, Step, RunRequest
class selClockTaskByType(HttpRunner):
    config = (
        Config("#活动页-根据类型进入跑步/读书/其他")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                           "number": {
                                    "body":{
                                            "pageNum": "$pageNum",
                                            "pageSize": "$pageSize",
                                            "type": "$type"            # 2>读书打卡   3>跑步打卡  4>其他打卡
                                            },
                                    "header":{"appType":"4"}
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
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].markTaskType","markTaskType")    #提取出第一个的习惯打卡的类型type
                .validate()
                .assert_equal("body.message", "$message")
                .assert_equal("body.body[0].markTaskType", "$markTaskType")   #判断出第一个的习惯打卡的类型type

        )
    ]

if __name__ == '__main__':
    selClockTaskByType().test_start()