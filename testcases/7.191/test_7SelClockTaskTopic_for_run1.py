from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.stdLearnInfo import stdLearnInfo

class TestCasesSelClockTaskTopic_for_run(HttpRunner):
    config = (
        Config("报跑步打卡的话术")
            .verify(False)
            .variables(**{
                            "markTaskType": "3",
                            "topicName":"#amylee跑步测试勿删#",               #校验的话题词
                            "message": "success",
                        }
                       )
            )
    teststeps = [
        Step(RunTestCase("习惯默认带出习惯话题").setup_hook('${update_task(905,906)}').call(SelClockTaskTopic)),
                 ]

if __name__ == '__main__':
    TestCasesSelClockTaskTopic_for_run().test_start()