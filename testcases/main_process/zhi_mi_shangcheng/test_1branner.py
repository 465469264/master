from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.userHome import get_info
from api.app.getAppBanner import getAppBanner


class Test_shangcheng_branner(HttpRunner):
    config = (
        Config("智米商城branner")
            .verify(False)
            .variables(**{
                        "message": "success"
                }
                       )
    )
    teststeps = [
        Step(RunTestCase("智米商城branner").call(getAppBanner)),

    ]
if __name__ == '__main__':
    Test_shangcheng_branner().test_start()