from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
#直播间赠送智米
class usRewardGift(HttpRunner):
    config = (
        Config("直播间赠送智米")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
            "number": {
                        "header": {
                            "appType": "4",
                        },
                        "body": {
                            "mappingId": "$mappingId",                           #打赏对应的课次ID
                            "money": "$money",                                    #学员打赏礼物价值
                            "giftName": "$giftName",                              #礼品名称
                            "iOS_version": "7.19.6",
                            "teaEmpName": "$teaEmpName",                         #老师姓名
                            "courseTimeName": "$courseTimeName",                #打赏课时名称
                            "stuLearnId": "$stuLearnId",
                            "teaEmpId": "$teaEmpId",                           #老师员工id
                            "sourceType": "$sourceType",                            #打赏来源类型 1: 课程 2: 直播广场
                            "type": "$type",                              #1 辅导课, 2 学科课, 3 自考课, 4 国开课   5>赠送智米
                            "stuUserName": "$stuUserName",
                            "giftType": "$giftType",                  #1>智米
                        }
                    },
            "data": "${base64_encode($number)}"
        })
    )
    teststeps = [
        Step(
            RunRequest("直播间赠送智米")
            .post("/proxy/mkt/usRewardGift/1.0/")
            .with_headers(
                **{
                    "authtoken": "${ENV(app_auth_token)}",
                    "Content-Type": "text/yzedu+; charset=UTF-8",
                }
            )
            .with_data('$data')
            .extract()
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]


if __name__ == "__main__":
    usRewardGift().test_start()