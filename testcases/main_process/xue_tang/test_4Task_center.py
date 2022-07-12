from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.stdLearnInfo import stdLearnInfo
from api.app.getNotReadTasksCounts import getNotReadTasksCounts
from api.app.myTasks import myTasks
from api.app.updateTaskReadStatus import updateTaskReadStatus

class Task_center(HttpRunner):
    config = (
        Config("任务中心")
            .verify(False)
            .variables(**{
                            "message": "success",
                            }
                       )
            )
    teststeps = [
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("任务中心列表的所有任务").call(myTasks).export(*["taskId"])),
        Step(RunTestCase("获取未读的任务").setup_hook("${student_task($taskId)}").call(getNotReadTasksCounts)),
        Step(RunTestCase("修改任务中心中的任务为已读").call(updateTaskReadStatus)),

    ]
if __name__ == '__main__':
    Task_center().test_start()