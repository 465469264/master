#圈子页-读书页
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.userHome import get_info
from api.app.selCommonlyUsedBooks import selCommonlyUsedBooks
from api.app.selCircleDynamicInfos import selCircleDynamicInfos


class TestCaseCircle_My_read_book(HttpRunner):
    config = (
        Config("圈子页-读书记录")
            .verify(False)
            .variables(**{
                            "message": "success"
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取用户信息，获取userId").call(get_info).export(*["userId"])),
        Step(RunTestCase('圈子-读书页-用户读过的书').call(selCommonlyUsedBooks).export(*["bookId"])),
                ]

if __name__ == "__main__":
    TestCaseCircle_My_read_book().test_start()

