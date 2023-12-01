#邀约海报
from httprunner import HttpRunner, Config, Step, RunRequest
class Iinvite_GetInvitationQRCode(HttpRunner):
    config = (
        Config("邀约海报")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                        "sceneJson": "{\"inviteToken\":\"${ENV(app_auth_token)}\","
                                                     "\"inviteMobile\":\"${read_data_number(ApplyRecord,mobile)}\","
                                                     "\"circleId\":\"$circleId\","                     #邀约的帖子
                                                     "\"regOrigin\":\"$regOrigin\""                    #邀约类型  1>帖子
                                                     "}",
                                        "page": "$page"                               #小程序的跳转路径
                                    },
                                        "header":{"appType":"${ENV(appType)}"}
                                    },
                          "data": "${base64_encode($number)}",
                          }
                       )
    )
    teststeps = [
        Step(
            RunRequest("邀约海报")
                .post("/proxy/invite/getInvitationQRCode/1.0/")
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
