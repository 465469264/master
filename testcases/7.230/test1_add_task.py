#学服任务版本，2023、1、30上线。学服任务的置顶排序，完成时间排序，以及新增过期/废弃类型
from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.web.studyActivity_toEdit_web_token import studyActivity_toEdit  #获取新增学服任务的_web_token
from api.web.task_taskUpdate import task_taskUpdate
from api.app.stdLearnInfo import stdLearnInfo
from api.web.studyActivity_list import studyActivity_list
from api.web.task_addStu import task_addStu

class Test_student_task(HttpRunner):
    config = (
        Config("新增学服任务")
            .verify(False)
            .variables(**{
                        "exType":"Add",
                        "message": "success",
                        "taskTitle":"自动化测试新增",
                        "startTimeInput":"${now_times()}",
                        "startTime":"${now_times()}",
                        "endTimeInput":"${day_late()}",
                        "endTime":"${day_late()}",
                        "taskType":"1",                          #1>任务通知型
                        "isAllow": "1",  # 是否启用             禁用>0             启用>1
                        "isNeedCheck": "0",  # 是否需毕业核查       不核查>0      置顶1
                        "isSticky": "1",  # 是否APP和公众号置顶  不置顶>0     置顶>1
                        "isStudentSee": "1",  # 对学生可见         不可见>0        可见>1
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取新增学服任务的_web_token").setup_hook('${login_web()}', "Cookie").call(studyActivity_toEdit).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token","Cookie"])),
        Step(RunTestCase("新增学服置顶的学服任务").call(task_taskUpdate)),
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("学服任务列表").call(studyActivity_list).export(*["taskId"])),
        Step(RunTestCase("添加学员至新建的学服任务").call(task_addStu)),

        #添加非置顶，学员可见
        Step(RunTestCase("添加非置顶，学员可见学服任务").with_variables(**({"isSticky": "0"})).call(task_taskUpdate)),
        Step(RunTestCase("学服任务列表").call(studyActivity_list).export(*["taskId"])),
        Step(RunTestCase("添加学员至新建的学服任务").call(task_addStu)),

        #添加已失效的任务
        Step(RunTestCase("添加非置顶，学员可见学服任务").with_variables(**({"isAllow": "0"})).call(task_taskUpdate)),
        Step(RunTestCase("学服任务列表").call(studyActivity_list).export(*["taskId"])),
        Step(RunTestCase("添加学员至新建的学服任务").call(task_addStu)),
    ]
if __name__ == '__main__':
    Test_student_task().test_start()