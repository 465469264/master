from httprunner import HttpRunner, Config, Step, RunRequest

#修改学生成绩
class updateStudentTScore(HttpRunner):
    config = (
        Config("获取学生的期末成绩")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("修改学生成绩")
                .post("/studentTScore/updateStudentTScore.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"$Cookie",

            })
                .with_data({
                            "learnId": "$learnId",
                            "stdId": "$stdId",
                            "grade": "$grade",
                            "_web_token": "$_web_token",
                            "recruitType": "$recruitType",
                            "semester": "$semester",
                            "scores[$a].courseId": "$courseId",
                            "scores[$a].courseName": "$courseName",
                            "scores[$a].examSubjectName": "$examSubjectName",
                            "scores[$a].advScore": "$advScore",                      #上进分
                            "scores[$a].usualTimeMark": "$usualTimeMark",            #平时成绩
                            "scores[$a].score": "$score",                            #卷面分
                            "scores[$a].totalmark": "$totalmark",                     #期末总分
                            "scores[$a].rewardScore": "$rewardScore",                #学业奖励分
                            "scores[$a].totalRewardScore": "$totalRewardScore",       #总分+奖励分
                            "scores[$a].teacherId": "$teacherId",                    #老师id
                            "scores[$a].teacher": "$teacher",                        #老师姓名
                            "scores[$a].examStatus": "$examStatus",                  #状态： 1>补考  2>缓考    3>缺考   4>正常   5>作弊
                             "scores[$a].courseScoreType": "$courseScoreType",       #课程类型   1>常规课程    2>校派课程
    }
                            )
                .extract()
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    updateStudentTScore().test_start()