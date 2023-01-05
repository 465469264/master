from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.web.studentTScore_findAllStudentTScore import studentTScore_findAllStudentTScore
from api.web.studentTScore_edit import studentTScore_edit_token
from api.web.studentTScore_findStudentTScoreBySemester import findStudentTScoreBySemester
from api.web.studentTScore_updateStudentTScore import updateStudentTScore
from api.app.loginOrRegister import app_login
from api.app.selStdAchievement import selStdAchievement

class TestCasesActivity_sendAppMsg(HttpRunner):
    config = (
        Config("修改第一学期的科目三，4，校派课程成绩")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(ApplyRecord,mobile)}",
            "semester": "1",
            "message": "success",

        })
            )
    teststeps = [
        # 科目3:校派课程-卷面成绩60分，及格
        Step(RunTestCase("用手机号查询学生信息").setup_hook('${login_web()}', "Cookie").call(studentTScore_findAllStudentTScore).export(*["learnId","grade","stdId","recruitType","Cookie"])),
        Step(RunTestCase("获取编辑学生成绩的web_token").call(studentTScore_edit_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("获取学生第一期-科目1成绩").call(findStudentTScoreBySemester).export(*["courseName","examSubjectName","courseId","totalmark","totalRewardScore","teacher","teacherId","advScore","usualTimeMark","score"])),
        Step(RunTestCase("编辑第一学期-科目1成绩-校派有50卷面分，学业奖励分20-正常状态").with_variables(**({"a":"0","score":"60","rewardScore":"20","examStatus":"4","courseScoreType":"2"})).call(updateStudentTScore)),
        Step(RunTestCase("修改后获取学生第一期-科目1成绩用来与APP的成绩对比").call(findStudentTScoreBySemester).export(*["score","rewardScore","totalRewardScore"])),
        Step(RunTestCase("对比学生科目1成绩").call(selStdAchievement)),



    ]
if __name__ == '__main__':
    TestCasesActivity_sendAppMsg().test_start()



