from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.loginOrRegister import app_login

class TestCasesSelClockTaskTopic_for_run(HttpRunner):
    config = (
        Config("老师+学员身份习惯读书笔记发帖话术")
            .verify(False)
            .variables(**{
                            "markTaskType": "2",
                            "message": "success",
                            }
                       )
            )
    teststeps = [
        Step(RunTestCase("默认带出读书绩效话题+读书习惯话题+习惯自动话术").with_variables(**({"markTaskType": "2"})).call(SelClockTaskTopic))
    ]

if __name__ == '__main__':
    TestCasesSelClockTaskTopic_for_run().test_start()