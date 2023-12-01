#成人高考报读
##页面的营销活动是写死的，有H5前端写死
from httprunner import HttpRunner, Config, Step, RunTestCase
from api.H5.RecruitUnvsList import RecruitUnvsList
from api.H5.FindPfsnByActId import findPfsnByActId
from api.H5.GetMarketingBanner import GetMarketingBanner
from api.H5.RcruitCityList import RecruitCityList
from api.H5.GetNewRegList import GetNewRegList


class Test_Enrollment_Study(HttpRunner):
    config = (
        Config("获取成教-专科升本科类-报读学校与专业-报读branna-已报读人轮播图")
            .verify(False)
            .variables(**{
                            "actId": "${read_data_number(actId,actId)}",
                            "pfsnLevel": "1",
                            "recruitType": "1",
                            "cityCode": "",
                            "pfsnName": "",
                            "message":"success"
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取大专-成人高考的banna图1").with_variables(**({"type": "8","bannerBelong": 1})).call(GetMarketingBanner)),
        Step(RunTestCase("获取大专-成人高考的banna图2").with_variables(**({"type": "ck_7","bannerBelong": 2})).call(GetMarketingBanner)),
        Step(RunTestCase("获取最新报读的轮播图").call(GetNewRegList)),
        Step(RunTestCase("获取1>专科升本科类可报名的所有城市").call(RecruitCityList)),
        Step(RunTestCase("获取1>专科升本科类可报名的大学").call(RecruitUnvsList)),
        Step(RunTestCase("获取专科升本科类可报名的专业").call(findPfsnByActId)),

    ]

if __name__ == "__main__":
    Test_Enrollment_Study().test_start()