from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.loginOrRegister import app_login
from api.app.stdLearnInfo import stdLearnInfo
from api.app.studentCertificateApply import getCertificateApply


class Test_Apply_Enrollment(HttpRunner):
    config = (
        Config("申请模块")
            .verify(False)
            .variables(**{
                "mobile": "${read_data_number(ApplyRecord,mobile)}"
                })
    )
    teststeps = [
        Step(RunTestCase("登录申请发票的手机号").call(app_login).export(*["app_auth_token","userId"])),
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId","std_name","unvsId","unvsName","grade"])),
        Step(RunTestCase("申请报读证明").with_variables(**({"stdName":"$std_name","userId":"$unvsId","applyType":"6","remark":"测试","applyPurpose":"测试","receiveType":"3","unvsName":"",
                                                                 "districtCode": "","district": "","city": "",
                                                                "cityCode": "","stampDown": "","receiveName": "",
                                                                "provinceCode": "","province": "","receiverName": "",
                                                                    "receiverMobile": "",
                                                                 "receiveMobile": "","receiveAddress": "","receiverAddress": "","materialName":"",
                                                            })).call(getCertificateApply)),
     #异常传参
        Step(RunTestCase("申请报读证明，不传备注").with_variables(**({"stdName": "$std_name", "userId": "$unvsId", "applyType": "6", "remark": "", "applyPurpose": "测试","receiveType": "3", "unvsName": "",
                                                                   "districtCode": "", "district": "", "city": "",
                                                                   "cityCode": "", "stampDown": "", "receiveName": "",
                                                                   "provinceCode": "", "province": "", "receiverName": "",
                                                                   "receiverMobile": "",
                                                                   "receiveMobile": "", "receiveAddress": "",
                                                                   "receiverAddress": "", "materialName": "",
                                                                    })).call(getCertificateApply)),
        Step(RunTestCase("申请报读证明，不传备注,不传申请用途").with_variables(**({"stdName": "$std_name", "userId": "$unvsId", "applyType": "6", "remark": "", "applyPurpose": "","receiveType": "3", "unvsName": "",
                                                                  "districtCode": "", "district": "", "city": "",
                                                                  "cityCode": "", "stampDown": "", "receiveName": "",
                                                                  "provinceCode": "", "province": "",
                                                                  "receiverName": "",
                                                                  "receiverMobile": "",
                                                                  "receiveMobile": "", "receiveAddress": "",
                                                                  "receiverAddress": "", "materialName": "",
                                                                  })).call(getCertificateApply)),
        Step(RunTestCase("申请报读证明，输入类型").with_variables(**({"stdName":"$std_name","userId":"$unvsId","applyType":"6","remark":"测试@@@123古典风格fffff","applyPurpose":"测试@@@123古典风格fffff测试@@@123古典风格fffff测试@@@123古典风格fffff","receiveType":"3","unvsName":"",
                                                           "districtCode": "", "district": "", "city": "",
                                                           "cityCode": "", "stampDown": "", "receiveName": "",
                                                           "provinceCode": "", "province": "", "receiverName": "",
                                                           "receiverMobile": "",
                                                           "receiveMobile": "", "receiveAddress": "",
                                                           "receiverAddress": "", "materialName": "",
                                                           })).call(getCertificateApply)),

    ]
if __name__ == '__main__':
    Test_Apply_Enrollment().test_start()



