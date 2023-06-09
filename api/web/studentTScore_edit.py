from httprunner import HttpRunner, Config, Step, RunRequest

# 获取编辑学生成绩token
class studentTScore_edit_token(HttpRunner):
    config = (
        Config("获取编辑学生成绩token")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("编辑学生成绩token")
                .post("/studentTScore/edit.do")
                .with_headers(**{
                "Accept":"*/*",
                "User-Agent":"PostmanRuntime/7.28.4",
                "Accept-Encoding":"gzip, deflate, br",
                "Connection":"keep-alive",
                "Cookie": "$Cookie",

    })
                .with_data({"learnId": "$learnId","recruitType":"$recruitType"})
                .extract()
                .with_jmespath("body","body") #获取body
        )
    ]