from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.newUsLivesScheduleInfos import newUsLivesScheduleInfos
from api.app.userHome import get_info
from api.app.isLiving import isLiving

class TestCasesLIive_poster(HttpRunner):
    config = (
        Config("app直播广场获取海报")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "id":"324"
                            }
                       )
            )
    teststeps = [
        Step(RunTestCase("获取用户信息，获取userId").call(get_info).export(*["userId"])),
        Step(RunTestCase("app直播广场获取海报").setup_hook('${Modify_lives_schedule($id)}').call(newUsLivesScheduleInfos)),
        Step(RunTestCase("APP获取是否有直播开启").with_variables(**({"isLiving":"1"})).call(isLiving)),


    ]

if __name__ == '__main__':
    TestCasesLIive_poster().test_start()