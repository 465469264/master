#登录APP查看学服任务，查看待完成，已完成，已失效的任务，并且点击
from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.myTasks import myTasks
from api.app.myTasks import myTasks2
from api.app.stdLearnInfo import stdLearnInfo
from api.app.updateTaskReadStatus import updateTaskReadStatus
from api.app.updateTaskStatus import updateTaskStatus


class Test_post_circle(HttpRunner):
    config = (
        Config("APP学服任务")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "scPicUrl":"",
                            "scText": "测试测试测试测试测试",
                            "scSource": "2"  # 帖子来源，1.安卓，2.iOS 3. 公众号 4.上进学社 5.红包
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取学员报读信息learnid").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase('获取用户学服任务').call(myTasks).export(*["taskId"])),
        Step(RunTestCase("任务中心中的任务为已读").call(updateTaskReadStatus)),
        Step(RunTestCase("更改学服任务状态，待完成>已完成").call(updateTaskReadStatus)),
        Step(RunTestCase("查看已完成列表").with_variables(**{"tabType": "1","taskStatus": "1"}).call(myTasks2)),
        Step(RunTestCase("查看已失效列表").with_variables(**{"tabType": "2","taskStatus": ""}).call(myTasks2)),

    ]
if __name__ == '__main__':
    Test_post_circle().test_start()