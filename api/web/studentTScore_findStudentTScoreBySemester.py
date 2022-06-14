from httprunner import HttpRunner, Config, Step, RunRequest

#获取学生的期末成绩
class findStudentTScoreBySemester(HttpRunner):
    config = (
        Config("获取学生的期末成绩")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("获取学生的期末成绩")
                .post("/studentTScore/findStudentTScoreBySemester.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"${ENV(COOKIE)}",
            })
                .with_data({
                            "learnId": "$learnId",
                            "semester":"$semester"
                            }
                            )
                .extract()
                .with_jmespath("body.body[0].courseName", "courseName")              #课程名称
                .with_jmespath("body.body[0].courseId", "courseId")                 # 课程id
                .with_jmespath("body.body[0].examSubjectName", "examSubjectName")    # 考试科目
                .with_jmespath("body.body[0].score", "score")                        #卷面分
                .with_jmespath("body.body[0].totalmark", "totalmark")                #期末总分
                .with_jmespath("body.body[0].rewardScore", "rewardScore")            #学业奖励分
                .with_jmespath("body.body[0].totalRewardScore", "totalRewardScore")    #总分+奖励分
                .with_jmespath("body.body[0].teacher", "teacher")                      #教师名字
                .with_jmespath("body.body[0].teacherId", "teacherId")                 # 教师ID
                .with_jmespath("body.body[0].advScore", "advScore")                   # 上进分
                .with_jmespath("body.body[0].usualTimeMark", "usualTimeMark")        # 平时成绩
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    findStudentTScoreBySemester().test_start()