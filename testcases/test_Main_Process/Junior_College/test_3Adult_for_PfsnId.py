#根据专业查询可报读学院
from httprunner import HttpRunner, Config, Step, RunTestCase
from api.H5.FindPfsnByActId import findPfsnByActId
from api.H5.FindUnvsByPfsnId import findUnvsByPfsnId


class Test_Find_By_PfsnByActId(HttpRunner):
    config = (
        Config("根据专业查询可报读学院")
            .verify(False)
            .variables(**{
                            "actId": "${read_data_number(actId,actId)}",
                            "grade": "${read_data_number(grade,grade)}",
                            "pfsnLevel": "1",          # 5>高中起点高职高专	，1>专科升本科类 6>硕士研究生，7>中专，8>高起本
                            "recruitType": "1",
                            "pfsnName": "",
                            "message":"success"
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取专科升本科类可报名的专业").call(findPfsnByActId).export(*["pfsnName"])),
        Step(RunTestCase("根据返回的第一个专业查询可报读学院").call(findUnvsByPfsnId)),

    ]

if __name__ == "__main__":
    Test_Find_By_PfsnByActId().test_start()