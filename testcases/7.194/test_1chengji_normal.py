from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.web.studentTScore_findAllStudentTScore import studentTScore_findAllStudentTScore
from api.web.studentTScore_edit import studentTScore_edit_token
from api.web.studentTScore_findStudentTScoreBySemester import findStudentTScoreBySemester
from api.web.studentTScore_updateStudentTScore import updateStudentTScore
from api.app.loginOrRegister import app_login
from api.app.selStdAchievement import selStdAchievement

class TestCasesActivity_sendAppMsg(HttpRunner):
    config = (
        Config("修改第一学期科目一，科目二的普通课程成绩")
            .verify(False)
            .variables(**{
            "mobile": "13166168256",
            "semester": "1",                 #获取学生目前的第一学期成绩
            "message": "success",

        })
            )
    teststeps = [
        # 科目1:奖励分20分，卷面成绩50分，及格
        Step(RunTestCase("用手机号查询学生信息").setup_hook('${login_web()}', "Cookie").call(studentTScore_findAllStudentTScore).export(*["learnId","grade","stdId","recruitType","Cookie"])),
        Step(RunTestCase("获取编辑学生成绩的web_token").call(studentTScore_edit_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("获取学生第一期-科目1成绩").call(findStudentTScoreBySemester).export(*["courseName","examSubjectName","courseId","totalmark","totalRewardScore","teacher","teacherId","advScore","usualTimeMark","score"])),
        Step(RunTestCase("编辑第一学期-科目1成绩-常规课程有50卷面分，学业奖励分20-正常状态").with_variables(**({"a":"0","score":"60","rewardScore":"20","examStatus":"4","courseScoreType":"1"})).call(updateStudentTScore)),
        Step(RunTestCase("修改后获取学生第一期-科目1成绩用来与APP的成绩对比").call(findStudentTScoreBySemester).export(*["score","rewardScore","totalRewardScore"])),
        Step(RunTestCase("对比学生科目1成绩").call(selStdAchievement)),

        # 科目1:卷面成绩50分，不及格
        Step(RunTestCase("获取编辑学生成绩的web_token").call(studentTScore_edit_token).teardown_hook('${get_html($body)}',"_web_token").export(*["_web_token"])),
        Step(RunTestCase("获取学生第一期-科目1成绩").call(findStudentTScoreBySemester).export(*["courseName","examSubjectName","courseId","totalmark","totalRewardScore","teacher","teacherId","advScore","usualTimeMark","score"])),
        Step(RunTestCase("编辑第一学期-科目1成绩-常规课程有50卷面分，学业奖励分20-正常状态").with_variables(**({"a":"0","score":"60","rewardScore":"","examStatus":"4","courseScoreType":"1"})).call(updateStudentTScore)),
        Step(RunTestCase("修改后获取学生第一期-科目1成绩用来与APP的成绩对比").call(findStudentTScoreBySemester).export(*["score", "rewardScore", "totalRewardScore"])),
        Step(RunTestCase("对比学生科目1成绩").call(selStdAchievement)),

        #科目2:奖励分20分，卷面成绩50分，补考
        Step(RunTestCase("获取编辑学生成绩的web_token").call(studentTScore_edit_token).teardown_hook('${get_html($body)}',"_web_token").export(*["_web_token"])),
        Step(RunTestCase("获取学生第一期-科目1成绩").call(findStudentTScoreBySemester).export(*["courseName","examSubjectName","courseId","totalmark","totalRewardScore","teacher","teacherId","advScore","usualTimeMark","score"])),
        Step(RunTestCase("编辑第一学期-科目1成绩-常规课程有50卷面分，学业奖励分20-正常状态").with_variables(**({"a":"0","score":"60","rewardScore":"","examStatus":"1","courseScoreType":"1"})).call(updateStudentTScore)),
        Step(RunTestCase("修改后获取学生第一期-科目1成绩用来与APP的成绩对比").call(findStudentTScoreBySemester).export(*["score", "rewardScore", "totalRewardScore"])),
        Step(RunTestCase("对比学生科目1成绩").call(selStdAchievement)),


    ]
if __name__ == '__main__':
    TestCasesActivity_sendAppMsg().test_start()



