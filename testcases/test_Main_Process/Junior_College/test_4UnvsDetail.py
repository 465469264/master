#报读大学的详情
from httprunner import HttpRunner, Config, Step, RunTestCase
from api.H5.RecruitUnvsList import RecruitUnvsList
from api.H5.UnvsDetail import UnvsDetail
from api.H5.UnvsIntroduce import UnvsIntroduce


class Test_UnvsDetail(HttpRunner):
    config = (
        Config("成教-专升本报读大学的详情")
            .verify(False)
            .variables(**{
                            "pfsnLevel": "1",          # 5>高中起点高职高专	，1>专科升本科类 6>硕士研究生，7>中专，8>高起本
                            "recruitType": "1",        #recruitType.1>成人教育 2>国家开放大学	3>全日制	 4>自考	5>硕士研究生  6>中专
                            "cityCode": "",
                            "message":"success"
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取成教-专科升本科类可报名的大学").call(RecruitUnvsList).export(*["unvsId"])),
        Step(RunTestCase("查询成教-专科升本科页面第一个大学详情").call(UnvsDetail)),
        Step(RunTestCase("查询成教-专科升本科页面第一个大学院校介绍").call(UnvsIntroduce)),

    ]

if __name__ == "__main__":
    Test_UnvsDetail().test_start()