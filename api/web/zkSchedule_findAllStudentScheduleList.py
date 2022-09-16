from httprunner import HttpRunner, Config, Step, RunRequest
#自考教务---自考学生排课
class zkSchedule_findAllStudentScheduleList(HttpRunner):
    config = (
        Config("自考教务---自考学生排课")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("自考教务---自考学生排课")
                .post("/zkSchedule/findAllStudentScheduleList.do")
                .with_headers(**{
                "Content - Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length": "246",
                "Host": "${ENV(Host)}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Cookie": "$Cookie"
                                }
                                )
                .with_data(
                            {
                            "length": "10",
                            "start": "0",

                            }
                            )
                .extract()
                .validate()
                .assert_equal("status_code", 200)
        )
]