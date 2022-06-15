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
            "mobile": "13001062741",
            "semester": "1"
        })
            )
    teststeps = [
        # 科目3:校派课程-卷面成绩60分，及格
        Step(RunTestCase("用手机号查询学生信息").call(studentTScore_findAllStudentTScore).export(*["learnId","grade","stdId","recruitType"])),
        Step(RunTestCase("获取编辑学生成绩的web_token").call(studentTScore_edit_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("获取学生第一期-科目3成绩").call(findStudentTScoreBySemester).export(*["courseName2","courseId2","totalmark2","totalRewardScore2","teacher2","teacherId2","advScore2","usualTimeMark2"])),
        Step(RunTestCase("编辑第一学期-科目3成绩-校派课程-只有卷面分").with_variables(**({"a":"2","score": "60", "rewardScore": "","examStatus": "4",
        "courseScoreType": "2", "examSubjectName": "$courseName2","courseId":"$courseId2","courseName":"$courseName2","advScore":"$advScore2","usualTimeMark":"$usualTimeMark2",
        "totalmark":"$totalmark2","totalRewardScore":"$totalRewardScore2","teacherId":"$teacherId2","teacher":"$teacher2"})).call(updateStudentTScore)),
        Step(RunTestCase("修改后获取学生第一期-科目3成绩用来与APP的成绩对比").call(findStudentTScoreBySemester).export(*["score2","rewardScore2"])),
        Step(RunTestCase("登录学生账号").call(app_login).export(*["app_auth_token"])),
        Step(RunTestCase("对比学生科目3成绩").with_variables(**({"a":"2","isPass":int("1"),"totalScore":"$score2","usualTimeMark":"$usualTimeMark2","score":"$score2","rewardScore":"$rewardScore2"})).call(selStdAchievement)),

        #科目四：校派课程-平时成绩20，卷面成绩60，补考
        Step(RunTestCase("获取编辑学生成绩的web_token").call(studentTScore_edit_token).teardown_hook('${get_html($body)}',"_web_token").export(*["_web_token"])),
        Step(RunTestCase("获取学生第一期-科目4成绩").call(findStudentTScoreBySemester).export(*["courseName3", "courseId3", "totalmark3", "totalRewardScore3", "teacher3", "teacherId3", "advScore3","usualTimeMark3"])),
        Step(RunTestCase("编辑第一学期-科目4成绩-校派课程-只有卷面分").with_variables(**({"a":"3", "score": "60", "rewardScore": "", "examStatus": "1","courseScoreType": "2", "examSubjectName": "$courseName3", "courseId": "$courseId3",
         "courseName": "$courseName3", "advScore": "$advScore3", "usualTimeMark": "20","totalmark": "$totalmark3", "totalRewardScore": "$totalRewardScore3", "teacherId": "$teacherId3","teacher": "$teacher3"})).call(updateStudentTScore)),
        Step(RunTestCase("修改后获取学生第一期-科目4成绩用来与APP的成绩对比").call(findStudentTScoreBySemester).export(*["score3", "rewardScore3","totalRewardScore3"])),
        Step(RunTestCase("登录学生账号").call(app_login).export(*["app_auth_token"])),
        Step(RunTestCase("对比学生科目4成绩").with_variables(**({"a":"3", "isPass": int("2"), "totalScore": "$totalRewardScore3", "usualTimeMark": "$usualTimeMark3", "score": "$score3","rewardScore": "$rewardScore3"})).call(selStdAchievement)),


    ]
if __name__ == '__main__':
    TestCasesActivity_sendAppMsg().test_start()



