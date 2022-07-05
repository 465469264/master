from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.selUsNewBookDetail import selUsNewBookDetail
from api.app.loginOrRegister import app_login

class TestCasesSelClockTaskTopic_for_read(HttpRunner):
    config = (
        Config("读书打卡带出书籍")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "name": "数星星的夜",
                            "markTaskType": "2"
                        }
                       )
            )
    teststeps = [
        Step(RunTestCase("带出书籍").call(selUsNewBookDetail))

    ]

if __name__ == '__main__':
    TestCasesSelClockTaskTopic_for_read().test_start()