import pytest,sys,os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.stdLearnInfo import stdLearnInfo
from api.app.studentCertificateApply import studentCertificateApply2
from api.app.getCertificateApply import getCertificateApply


class Test_Apply_Enrollment(HttpRunner):
    @pytest.mark.parametrize("param",Parameters({"remark-applyPurpose":"${Apply_Enrollment()}"}))
    def test_start(self,param):
        super().test_start(param)
    config = (
        Config("申请模块")
            .verify(False)
            .variables(**{
                "mobile": "${read_data_number(ApplyRecord,mobile)}"
                })
    )
    teststeps = [
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId","std_name","unvsId","unvsName","grade"])),
        Step(RunTestCase("申请报读证明").with_variables(**({"stdName": "$std_name","userId": "unvsId","applyType": "6","receiveType": "3","unvsName": ""})).call(studentCertificateApply2)),
        Step(RunTestCase("申请列表,其他申请证明为已完成").with_variables(**({"a": "0", "checkStatus": 3})).call(getCertificateApply)),
    ]
if __name__ == '__main__':
    Test_Apply_Enrollment().test_start()



