from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.loginOrRegister import app_login
from api.app.stdLearnInfo import stdLearnInfo
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.selUsNewBookDetail import selUsNewBookDetail
from api.app.usReadExt import usReadExt
from api.app.userHome import get_info


class Test_Read_habbit(HttpRunner):
    config = (
        Config("读书打卡话术-打卡")
            .verify(False)
            .variables(**{
            "taskId": "${read_data_number(SelClockTaskTopic_read,taskid)}",
            "localFile": "${read_data_number(SelClockTaskTopic_run,localFile)}",
            "bucketName": "yzimstemp",
            "markTaskType": "2",           #任务打卡类型：2：读书  3：跑步    4：其他
            "topicName":"#amylee读书打卡勿删测试#",
            "cycleType": "1",       #打卡周期类型 1: 连续 2：累计
            "subType": "1",         #普通贴：subType :0     1：读书贴  2：跑步贴）
            "scType": "2",           #读书社:scType.2,  跑团：scType.3，  自考圈：scType.4	，同学圈：scType.1   ，职场圈：scType.5
            "message": "success"

        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取信息").call(get_info).export(*["userId"])),
        Step(RunTestCase('获取用户报读信息').call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("默认带出读书绩效话题").call(SelClockTaskTopic).export(*["taskEnrollId","markContent"])),
        Step(RunTestCase("带出书籍").call(selUsNewBookDetail).export(*["name","imgUrl","readPersonNum","bookId"])),
        Step(RunTestCase("发贴读书习惯打卡帖子").call(usReadExt))

    ]
if __name__ == '__main__':
    Test_Read_habbit().test_start()