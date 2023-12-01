#生成跑步记录

from httprunner import HttpRunner, Config, Step, RunRequest
class usRunning(HttpRunner):
    config = (
        Config("生成跑步记录")
            .base_url("${ENV(app_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                        "runJson": "{\"runImg\":\"$scPicUrl\",\"runKmList\":[{\"runTime\":\"$runTime\",\"ifOneKm\":$ifOneKm}],\"stepFrequency\":\"$stepFrequency\",\"fastSpendDesc\":\"$fastSpendDesc\\\"\",\"runSecond\":\"$runSecond\",\"totalSteps\":\"$totalSteps\",\"spendDesc\":\"$spendDesc\\\"\",\"runStartTime\":\"2023-11-30 15:34:11\",\"slowSpendDesc\":\"$slowSpendDesc\\\"\",\"distance\":\"$distance\",\"trackFileUrl\":\"20231130033618983-483.txt\",\"runTime\":\"$runTime\"}"
                                        },
                                        "header":{"appType":"${ENV(appType)}"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("生成跑步记录")
                .post("/proxy/us/usRunning/1.0/")
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



