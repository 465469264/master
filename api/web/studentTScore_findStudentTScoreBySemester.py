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
                .with_jmespath("body.body[0].score", "score")                        #卷面分
                .with_jmespath("body.body[0].totalmark", "totalmark")                #期末总分
                .with_jmespath("body.body[0].rewardScore", "rewardScore")            #学业奖励分
                .with_jmespath("body.body[0].totalRewardScore", "totalRewardScore")    #总分+奖励分
                .with_jmespath("body.body[0].teacher", "teacher")                      #教师名字
                .with_jmespath("body.body[0].teacherId", "teacherId")                 # 教师ID
                .with_jmespath("body.body[0].advScore", "advScore")                   # 上进分
                .with_jmespath("body.body[0].usualTimeMark", "usualTimeMark")        # 平时成绩

                .with_jmespath("body.body[1].courseName", "courseName1")  # 课程名称
                .with_jmespath("body.body[1].courseId", "courseId1")  # 课程id
                .with_jmespath("body.body[1].score", "score1")  # 卷面分
                .with_jmespath("body.body[1].totalmark", "totalmark1")  # 期末总分
                .with_jmespath("body.body[1].rewardScore", "rewardScore1")  # 学业奖励分
                .with_jmespath("body.body[1].totalRewardScore", "totalRewardScore1")  # 总分+奖励分
                .with_jmespath("body.body[1].teacher", "teacher1")  # 教师名字
                .with_jmespath("body.body[1].teacherId", "teacherId1")  # 教师ID
                .with_jmespath("body.body[1].advScore", "advScore1")  # 上进分
                .with_jmespath("body.body[1].usualTimeMark", "usualTimeMark1")  # 平时成绩

                .with_jmespath("body.body[2].courseName", "courseName2")  # 课程名称
                .with_jmespath("body.body[2].courseId", "courseId2")  # 课程id
                .with_jmespath("body.body[2].score", "score2")  # 卷面分
                .with_jmespath("body.body[2].totalmark", "totalmark2")  # 期末总分
                .with_jmespath("body.body[2].rewardScore", "rewardScore2")  # 学业奖励分
                .with_jmespath("body.body[2].totalRewardScore", "totalRewardScore2")  # 总分+奖励分
                .with_jmespath("body.body[2].teacher", "teacher2")  # 教师名字
                .with_jmespath("body.body[2].teacherId", "teacherId2")  # 教师ID
                .with_jmespath("body.body[2].advScore", "advScore2")  # 上进分
                .with_jmespath("body.body[2].usualTimeMark", "usualTimeMark2")  # 平时成绩

                .with_jmespath("body.body[2].courseName", "courseName3")  # 课程名称
                .with_jmespath("body.body[2].courseId", "courseId3")  # 课程id
                .with_jmespath("body.body[2].score", "score3")  # 卷面分
                .with_jmespath("body.body[2].totalmark", "totalmark3")  # 期末总分
                .with_jmespath("body.body[2].rewardScore", "rewardScore3")  # 学业奖励分
                .with_jmespath("body.body[2].totalRewardScore", "totalRewardScore3")  # 总分+奖励分
                .with_jmespath("body.body[2].teacher", "teacher3")  # 教师名字
                .with_jmespath("body.body[2].teacherId", "teacherId3")  # 教师ID
                .with_jmespath("body.body[2].advScore", "advScore3")  # 上进分
                .with_jmespath("body.body[2].usualTimeMark", "usualTimeMark3")  # 平时成绩





                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    findStudentTScoreBySemester().test_start()