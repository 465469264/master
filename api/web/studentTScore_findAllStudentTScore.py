from httprunner import HttpRunner, Config, Step, RunRequest

# 期末成绩列表手机号查询学生
class studentTScore_findAllStudentTScore(HttpRunner):
    config = (
        Config("期末成绩列表手机号查询学生")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("期末成绩列表手机号查询学生")
                .post("/studentTScore/findAllStudentTScore.do")
                .with_headers(**{
                "Accept":"*/*",
                "User-Agent":"PostmanRuntime/7.28.4",
                "Accept-Encoding":"gzip, deflate, br",
                "Connection":"keep-alive",
                "Cookie": "${ENV(COOKIE)}",

    })
                .with_data({"mobile": "$mobile"})
                .extract()
                .with_jmespath("body.body.data[0].learnId","learnId")
                .with_jmespath("body.body.data[0].grade", "grade")
                .with_jmespath("body.body.data[0].stdId", "stdId")
                .with_jmespath("body.body.data[0].recruitType", "recruitType")
                .validate()
                .assert_equal("status_code", 200)

        )
    ]