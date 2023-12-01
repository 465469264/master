#报读本科-成教

from httprunner import HttpRunner, Config, Step, RunTestCase
from api.H5.GetActivityInfo import GetActivityInfo
from api.H5.EnrollInfo_unvsName import EnrollInfo_unvsName
from api.H5.EnrollInfo_pfsnLevelName import EnrollInfo_pfsnLevelName
from api.H5.EnrollInfo_pfsnName import EnrollInfo_pfsnName
from api.H5.RcruitCityList import RecruitCityList
from api.H5.EnrollInfo_taName import EnrollInfo_taName
from api.app.Register import Register
from api.web.editPhonecode import eddit_Phone_Message
from api.H5.Enroll import Enroll





class Test_Apply_Adult_Education(HttpRunner):
    config = (
        Config("报读本科-成教")
            .verify(False)
            .variables(**{
                            "mobile": "${get_not_exist_mobile()}",
                            "idCard": "${idcard()}",
                            "name": "${get_name()}",
                             "scholarship": "${read_data_number(scholarship,scholarship)}",    #优惠类型--前端写死
                            "pfsnLevel": "1",          # 5>高中起点高职高专	，1>专科升本科类 6>硕士研究生，7>中专，8>高起本
                            "recruitType": "1",        #recruitType.1>成人教育 2>国家开放大学	3>全日制	 4>自考	5>硕士研究生  6>中专
                            "grade": "2024",           #报读年级-前端写死
                            "cityCode": "",
                            "pageSize": "100",
                            "pageNum": "1",
                            "message":"success"
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("设置测试手机号码验证码").call(eddit_Phone_Message)),
        Step(RunTestCase("APP手机号注册-获取注册登录的token和手机号").call(Register).teardown_hook('${return_Cookie($headers)}', "Cookie").export(*["app_auth_token", "mobile", "userId","yzCode","Cookie"])),
        Step(RunTestCase("获取优惠类型").call(GetActivityInfo)),
        Step(RunTestCase("报读页面-可报读的院校").call(EnrollInfo_unvsName).export(*["unvsCode","unvsId","unvsName"])),
        Step(RunTestCase("报读页面-根据选择的院校-选择可选层次").call(EnrollInfo_pfsnLevelName).export(*["pfsnLevelName"])),
        Step(RunTestCase("报读页面-根据选择的院校-选择可选专业").call(EnrollInfo_pfsnName).export(*["pfsnName","pfsnId","pfsnCode"])),
        Step(RunTestCase("获取1>专科升本科类-可报名的所有城市").call(RecruitCityList).export(*["cityName","cityCode"])),
        Step(RunTestCase("获取1>专科升本科类-获取考试县区").with_variables(**({"taName":"$cityName"})).call(EnrollInfo_taName).export(*["taId","taName"])),
        Step(RunTestCase("报读").call(Enroll)),

    ]

if __name__ == "__main__":
    Test_Apply_Adult_Education().test_start()