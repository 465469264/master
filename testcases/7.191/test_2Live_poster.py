from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.usLivesScheduleInfos import TestZhibo

class TestCasesLIive_poster(HttpRunner):
    config = (
        Config("app直播广场获取海报")
            .verify(False)
            .variables(**{
        })
            )
    teststeps = [
        Step(RunTestCase("app直播广场获取海报").setup_hook('${delay(1)}').call(TestZhibo)),
                 ]

if __name__ == '__main__':
    TestCasesLIive_poster().test_start()