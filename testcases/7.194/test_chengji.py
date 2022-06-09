from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.web.studentTScore_findAllStudentTScore import studentTScore_findAllStudentTScore
from api.web.studentTScore_edit import studentTScore_edit_token
from api.web.studentTScore_findStudentTScoreBySemester import findStudentTScoreBySemester
from api.web.studentTScore_updateStudentTScore import updateStudentTScore


class TestCasesActivity_sendAppMsg(HttpRunner):
    config = (
        Config("获取平时成绩")
            .verify(False)
            .variables(**{
            "mobile": "18925547096",
            "semester": "1"
        })
            )
    teststeps = [
        Step(RunTestCase("用手机号查询学生信息").call(studentTScore_findAllStudentTScore).export(*["learnId","grade","stdId","recruitType"])),
        Step(RunTestCase("获取编辑学生成绩的web_token").call(studentTScore_edit_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("获取学生第一期成绩").with_variables(**({"semester":"1"})).call(findStudentTScoreBySemester).export(*["courseName","courseId","examSubjectName",
                                                                                                                      "teacher","teacherId","advScore","usualTimeMark","totalmark"])),
        Step(RunTestCase("编辑第一学期成绩-常规课程有卷面分，学业奖励分20-正常状态").with_variables(**({"score":"50","rewardScore":"20","totalRewardScore":"$totalmark",
                                                                              "examStatus":"4","courseScoreType":"1"})).call(updateStudentTScore)),
        Step(RunTestCase("编辑第一学期成绩-常规课修改卷面分>100，学业奖励分0-正常状态").with_variables(**({"score":"100","rewardScore":"0","totalRewardScore":"$totalmark",
                                                                              "examStatus":"4","courseScoreType":"1"})).call(updateStudentTScore))


    ]
if __name__ == '__main__':
    TestCasesActivity_sendAppMsg().test_start()



