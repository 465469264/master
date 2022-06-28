from httprunner import HttpRunner, Config, Step, RunRequest
#获取圈子数据
class selCircleDynamicInfos(HttpRunner):
    config = (
        Config("获取圈子数据")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            # "scType": "$scType",                         #读书社:scType.2,  跑团：scType.3，  自考圈：scType.4	，同学圈：scType.1   ，职场圈：scType.5
                                            "own": "0",                     #不知道什么字段
                                            "pageSize": "$pageSize",            #尺寸
                                            "userRoleType": "$userRoleType",       #账号身份         2>员工，4>学员   6>老师+学员  0>没有报读
                                            "userId": "$userId",
                                            "version": "1",                   #不知道什么字段
                                            "pageNum": "$pageNum",          #页码

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
            RunRequest("获取圈子数据")
                .post("/proxy/us/selCircleDynamicInfos/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",

                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    selCircleDynamicInfos().test_start()