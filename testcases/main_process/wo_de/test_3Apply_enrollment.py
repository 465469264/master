from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.loginOrRegister import app_login
from api.app.stdLearnInfo import stdLearnInfo
from api.app.studentCertificateApply import studentCertificateApply2
from api.app.getCertificateApply import getCertificateApply


class Test_Apply_Enrollment(HttpRunner):
    config = (
        Config("申请模块")
            .verify(False)
            .variables(**{
                "mobile": "${read_data_number(ApplyRecord,mobile)}"
                })
    )
    teststeps = [
        Step(RunTestCase("登录申请学员报读的手机号").call(app_login).export(*["app_auth_token","userId"])),
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId","std_name","unvsId","unvsName","grade"])),
        Step(RunTestCase("申请报读证明").with_variables(**({"stdName":"$std_name","userId":"$unvsId","applyType":"6","remark":"测试",
                                                      "applyPurpose":"测试","receiveType":"3","unvsName":""})).call(studentCertificateApply2)),
        Step(RunTestCase("申请列表,其他申请证明为已完成").with_variables(**({"a": "0", "checkStatus": 3})).call(getCertificateApply)),

        # 异常传参
        Step(RunTestCase("申请报读证明，不传备注").with_variables(**({"stdName": "$std_name", "userId": "$unvsId", "applyType": "6", "remark": "",
                                                           "applyPurpose": "测试","receiveType": "3", "unvsName": "",})).call(studentCertificateApply2)),
        Step(RunTestCase("申请报读证明，不传备注,不传申请用途").with_variables(**({"stdName": "$std_name", "userId": "$unvsId", "applyType": "6", "remark": "",
                                                                  "applyPurpose": "","receiveType": "3", "unvsName": "",})).call(studentCertificateApply2)),
        Step(RunTestCase("申请报读证明，输入类型").with_variables(**({"stdName":"$std_name","userId":"$unvsId","applyType":"6","remark":"测试@@@123古典风格fffff",
                                                           "applyPurpose":"测试@@@123古典风格fffff测试@@@123古典风格fffff测试@@@123古典风格fffff","receiveType":"3","unvsName":"",})).call(studentCertificateApply2)),

    ]
if __name__ == '__main__':
    Test_Apply_Enrollment().test_start()



