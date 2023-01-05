import pytest,sys,os
from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
print(str(Path(__file__).parent.parent.parent.parent))
from api.web.studentTScore_findAllStudentTScore import studentTScore_findAllStudentTScore
from api.web.studentTScore_edit import studentTScore_edit_token
from api.web.studentTScore_findStudentTScoreBySemester import findStudentTScoreBySemester
from api.web.studentTScore_updateStudentTScore import updateStudentTScore


class Test_cheng_ji(HttpRunner):
    @pytest.mark.parametrize("param",Parameters({"title-score-rewardScore-examStatus-courseScoreType":"${chengji()}"}))
    def test_start(self,param):
        super().test_start(param)
    config = (
        Config("平时成绩的--分数与类型字段测试")
            .verify(False)
            .variables(**{
                        "mobile": "13580270276",
                        "semester": "1",
                        "a": "0"
                            }
                       )
            )
    teststeps = [
        Step(RunTestCase("用手机号查询学生信息").setup_hook('${login_web()}', "Cookie").call(studentTScore_findAllStudentTScore).export(*["learnId","grade","stdId","recruitType","Cookie"])),
        Step(RunTestCase("获取编辑学生成绩的web_token").call(studentTScore_edit_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("获取学生第一期-科目1成绩").call(findStudentTScoreBySemester).export(
            *["courseName", "examSubjectName", "courseId", "totalmark", "totalRewardScore", "teacher", "teacherId",
              "advScore", "usualTimeMark", "score"])),
        Step(RunTestCase("平时成绩用例测试").call(updateStudentTScore)),
                ]
if __name__ == '__main__':
    Test_cheng_ji().test_start()