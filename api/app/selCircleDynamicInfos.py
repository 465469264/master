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
                                            "own": "$own",                     #0>只返回自己发的帖子，  1>返回评论/点赞他人，及自己发的帖子          查看最新或者跑团/同学圈/最新/时传空
                                            "scType": "$scType",                     #圈子  0>关注  1>同学圈  2>读书社  3>跑团  4>自考圈       查看自己圈子/别人圈子时/最新圈子时不传
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
                .with_jmespath("body.body[0].id", "id")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]


# 用于查看自己的主页
class selCircleDynamicInfos2(HttpRunner):
    config = (
        Config("获取圈子数据")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "own": "$own",                     #0>只返回自己发的帖子，  1>返回评论/点赞他人，及自己发的帖子          查看最新或者跑团/同学圈/最新/时传空
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
                .with_jmespath("body.body[0].id", "id")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]

if __name__ == '__main__':
    selCircleDynamicInfos().test_start()