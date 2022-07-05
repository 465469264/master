from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.usLivesScheduleInfos import TestZhibo
from api.app.userHome import get_info
from api.app.isLiving import isLiving

class TestCasesLIive_poster(HttpRunner):
    config = (
        Config("app直播广场获取海报")
            .verify(False)
            .variables(**{
            "message": "success",
        })
            )
    teststeps = [
        Step(RunTestCase("获取用户信息，获取userId").call(get_info).export(*["userId"])),
        Step(RunTestCase("app直播广场获取海报").setup_hook('${delay(1)}','${Modify_lives_schedule()}').call(TestZhibo)),
        Step(RunTestCase("APP获取是否有直播开启").with_variables(**({"isLiving":"1"})).call(isLiving)),


    ]

if __name__ == '__main__':
    TestCasesLIive_poster().test_start()