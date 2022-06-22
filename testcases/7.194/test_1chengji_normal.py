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
            "mobile": "13001062741",
            "semester": "1"
        })
            )
    teststeps = [
        # 科目1:奖励分20分，卷面成绩50分，及格
        Step(RunTestCase("用手机号查询学生信息").setup_hook('${login_web()}', "Cookie").call(studentTScore_findAllStudentTScore).export(*["learnId","grade","stdId","recruitType","Cookie"])),
        Step(RunTestCase("获取编辑学生成绩的web_token").call(studentTScore_edit_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("获取学生第一期-科目1成绩").call(findStudentTScoreBySemester).export(*["courseName","courseId","totalmark","totalRewardScore","teacher","teacherId","advScore","usualTimeMark"])),
        Step(RunTestCase("编辑第一学期-科目1成绩-常规课程有卷面分，学业奖励分20-正常状态").with_variables(**({"a":"0","score":"50","rewardScore":"20","examStatus":"4","courseScoreType":"1","examSubjectName":"$courseName"})).call(updateStudentTScore)),
        Step(RunTestCase("修改后获取学生第一期-科目1成绩用来与APP的成绩对比").call(findStudentTScoreBySemester).export(*["score","rewardScore","totalRewardScore"])),
        Step(RunTestCase("登录学生账号").call(app_login).export(*["app_auth_token"])),
        Step(RunTestCase("对比学生科目1成绩").with_variables(**({"a":"0","isPass":int("1"),"totalScore":"$totalRewardScore"})).call(selStdAchievement)),

        # # 科目1:卷面成绩50分，不及格
        Step(RunTestCase("获取编辑学生成绩的web_token").call(studentTScore_edit_token).teardown_hook('${get_html($body)}',"_web_token").export(*["_web_token"])),
        Step(RunTestCase("获取学生第一期-科目1成绩").call(findStudentTScoreBySemester).export(*["courseName","courseId","totalmark","totalRewardScore","teacher","teacherId","advScore","usualTimeMark"])),
        Step(RunTestCase("编辑第一学期-科目1成绩-常规课程有卷面分，正常状态").with_variables(**({"a":"0","score": "50", "rewardScore": "", "examStatus": "4", "courseScoreType": "1","examSubjectName": "$courseName"})).call(updateStudentTScore)),
        Step(RunTestCase("修改后获取学生第一期-科目1成绩用来与APP的成绩对比").call(findStudentTScoreBySemester).export(*["score", "rewardScore", "totalRewardScore"])),
        Step(RunTestCase("对比学生科目1成绩").with_variables(**({"a":"0","isPass": int("2"), "totalScore": "$totalRewardScore"})).call(selStdAchievement)),
        #
        #科目2:奖励分20分，卷面成绩50分，补考
        Step(RunTestCase("获取编辑学生成绩的web_token").call(studentTScore_edit_token).teardown_hook('${get_html($body)}',"_web_token").export(*["_web_token"])),
        Step(RunTestCase("获取学生第一期-科目2成绩").call(findStudentTScoreBySemester).export(*["courseName1","courseId1","courseName1","advScore1","usualTimeMark1","totalmark1","totalRewardScore1","teacherId1","teacher1"])),
        Step(RunTestCase("编辑第一学期-科目2成绩-常规课程有卷面分，补考状态").with_variables(**({"a":"1","score": "50", "rewardScore": "20","examStatus": "1",
        "courseScoreType": "1", "examSubjectName": "$courseName1","courseId":"$courseId1","courseName":"$courseName1","advScore":"$advScore1","usualTimeMark":"$usualTimeMark1",
        "totalmark":"$totalmark1","totalRewardScore":"$totalRewardScore1","teacherId":"$teacherId1","teacher":"$teacher1"})).call(updateStudentTScore)),
        Step(RunTestCase("修改后获取学生第一期-科目2成绩用来与APP的成绩对比").call(findStudentTScoreBySemester).export(*["score1", "rewardScore1"])),
        Step(RunTestCase("对比学生科目2成绩").with_variables(**({"a":"1","isPass": int("2"), "totalScore": "$score1","score":"$score1","rewardScore":"$rewardScore1"})).call(selStdAchievement)),


    ]
if __name__ == '__main__':
    TestCasesActivity_sendAppMsg().test_start()



