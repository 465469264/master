from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.getLearnInfoByLearnId import getLearnInfoByLearnId
from api.app.stdLearnInfo import stdLearnInfo
from api.app.selCourseList import selCourseList
from api.app.selCourseTimeById import selCourseTimeById
from api.app.getStageName import getStageName

class Test_qiandao(HttpRunner):
    config = (
        Config("用户切换学籍")
            .verify(False)
            .variables(**{
                            "message": "success",
                            }
                       )
            )
    teststeps = [
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("获取当前学籍信息").call(getLearnInfoByLearnId)),
        Step(RunTestCase("返回课程名称").call(selCourseList)),
        Step(RunTestCase("查询所有课程的有效时间").with_variables(**({"courseId":""})).call(selCourseTimeById).export(*["courseId"])),
        Step(RunTestCase("根据课程id，获取课程阶段").call(getStageName)),
        Step(RunTestCase("查询课程下的所有课时").call(selCourseTimeById)),

    ]
if __name__ == '__main__':
    Test_qiandao().test_start()