#读书计划-发帖
from httprunner import HttpRunner, Config, Step, RunTestCase
from api.app.selUsNewBookDetail import selUsNewBookDetail
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.usNewReadExt import UsNewReadExt

from api.app.userHome import get_info


class Test_Shangjin_Run(HttpRunner):
    config = (
        Config("读书计划-发帖")
            .verify(False)
            .variables(**{
                            "markTaskType": "2",  # 任务打卡类型：2：读书  3：跑步    4：其他
                            "cycleType": "0",           #0：无  打卡周期类型 1: 连续 2：累计
                            "subType": "1·",  # 帖子二级类型（1：读书贴  2：跑步贴）
                            "scType": "2",  # 圈子类型    0  => 首页 1  => 同学圈 2  => 读书会 3  => 跑团圈 4  => 自考圈
                            "message":"success",
                            "msg": "请求成功",
                            "scText": "${read_data_number(read_book,scText)}",

        }
                       )
    )
    teststeps = [
        Step(RunTestCase("APP获取个人信息").call(get_info).export(*["nickname", "realName", "userCircleRole", "stdName","userId"])),
        Step(RunTestCase("带出书本").call(selUsNewBookDetail).export(*["name","imgUrl","readPersonNum","bookId"])),
        Step(RunTestCase("习惯话题").call(SelClockTaskTopic).export(*["markContent"])),
        Step(RunTestCase("读书发帖").with_variables(**({"mappingId":"$bookId"})).call(UsNewReadExt)),

    ]

if __name__ == "__main__":
    Test_Shangjin_Run().test_start()