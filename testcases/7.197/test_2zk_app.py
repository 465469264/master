from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.zkStuServiceStatus import zkStuServiceStatus
from api.app.stdLearnInfo import stdLearnInfo


#获取自考服务期状态
class Test_zkStuServiceStatus(HttpRunner):
    config = (
        Config("获取自考服务期状态")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "msgType": "1",
                            "sourceType": "2",
                        }
                       )
                )
    teststeps = [
        Step(RunTestCase("获取learnId").call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("获取自考服务期状态").call(zkStuServiceStatus)),
                 ]

if __name__ == '__main__':
    Test_zkStuServiceStatus().test_start()