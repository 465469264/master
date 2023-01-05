#圈子页-我的视频
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.userHome import get_info
from api.app.selCommonlyUsedBooks import selCommonlyUsedBooks
from api.app.selCircleVideoInfo import selCircleVideoInfo


class TestCaseCircle_My_video(HttpRunner):
    config = (
        Config("圈子页-读书记录")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "pageSize": "1",
                            "pageNum": "20"
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取用户信息，获取userId").call(get_info).export(*["userId","ruleType"])),
        Step(RunTestCase('圈子页-我的视频').with_variables(**{"userRoleType":"$ruleType"}).call(selCircleVideoInfo)),
                ]

if __name__ == "__main__":
    TestCaseCircle_My_video().test_start()

