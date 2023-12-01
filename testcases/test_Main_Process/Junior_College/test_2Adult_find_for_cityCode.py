#成人教育-专科升本科类-根据城市搜索可报读学校
from httprunner import HttpRunner, Config, Step, RunTestCase
from api.H5.RecruitUnvsList import RecruitUnvsList
from api.H5.FindPfsnByActId import findPfsnByActId
from api.H5.GetMarketingBanner import GetMarketingBanner
from api.H5.RcruitCityList import RecruitCityList


class Test_find_for_cityCode(HttpRunner):
    config = (
        Config("获取成教-专科升本科类-报读学校与专业")
            .verify(False)
            .variables(**{
                            "actId": "${read_data_number(actId,actId)}",
                            "pfsnLevel": "1",
                            "recruitType": "1",
                            "pfsnName": "",
                            "cityCode": "",
                            "message":"success"
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取专科升本科类可报名的专业").call(findPfsnByActId)),
        Step(RunTestCase("根据专业查询可选学院").call(RecruitUnvsList)),

    ]

if __name__ == "__main__":
    Test_find_for_cityCode().test_start()