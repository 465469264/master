from httprunner import HttpRunner, Config, Step, RunRequest
#获取圈子页的活动列表
class selUpwardActivityInfo(HttpRunner):
    config = (
        Config("获取圈子页的活动列表")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                            "type":"$type",            #不传时，获取所有    1>报名中  2>进行中   3>已结束
                                    },
                                    "header": {"appType": "${ENV(appType)}"}
                          },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("获取圈子页的活动列表")
                .post("/proxy/mkt/selUpwardActivityInfo/1.0/")
                .with_headers(**{
                                    "User-Agent": "${ENV(User-Agent)}",
                                    "Content-Type": "text/yzedu+; charset=UTF-8",
                                    "Host": "${ENV(app_Host)}",
                                    "authtoken": "${ENV(app_auth_token)}",
                }
            )
                .with_data('$data')
                .extract()
                .with_jmespath("body.body[0].id", "actId")                #活动id
                .with_jmespath("body.body[0].actName", "actName")       #活动名称
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]





if __name__ == '__main__':
    selUpwardActivityInfo().test_start()
