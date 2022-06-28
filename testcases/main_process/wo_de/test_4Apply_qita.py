from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.loginOrRegister import app_login
from api.app.stdLearnInfo import stdLearnInfo
from api.app.studentCertificateApply import studentCertificateApply
from api.app.getJDProvince import GetJDProvince
from api.app.getJDCity import getJDCity
from api.app.getJDCounty import getJDCounty
from api.app.editAddress import eddit_address
from api.app.getCertificateApply import getCertificateApply
from api.web.certificate_findAllList import certificate_findAllList
from api.web.certificate_fdyCheck import fdyCheck

class Test_Apply_qita(HttpRunner):
    config = (
        Config("申请其他证明")
            .verify(False)
            .variables(**{
                "mobile": "${read_data_number(ApplyRecord,mobile)}"
                })
    )
    teststeps = [
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId","std_name","unvsId","unvsName","grade"])),
        Step(RunTestCase("获取省份").call(GetJDProvince).export(*["provinceCode","provinceName"])),
        Step(RunTestCase("获取城市").with_variables(**({"id":"$provinceCode"})).call(getJDCity).export(*["cityCode","cityName"])),
        Step(RunTestCase("地区").with_variables(**({"id":"$cityCode"})).call(getJDCounty).export(*["districtCode","districtName"])),
        Step(RunTestCase("编辑收货地址").with_variables(**({"saName":"测试","address":"测试地址","saType":"3","excType":"2","email":"123@qq.com"})).call(eddit_address)),

        Step(RunTestCase("申请其他证明").with_variables(**({
                                                            "checkStatus": "",
                                                            "stdName": "$std_name",
                                                            "userId": "$unvsId",
                                                            "applyType": "5",
                                                            "remark": "测试",
                                                            "applyPurpose": "测试",
                                                            "receiveType": "1",
                                                            "unvsName": "",
                                                            "district": "$districtName",
                                                            "city": "$cityName",
                                                            "stampDown": "1",
                                                            "receiveName": "测试",
                                                            "province": "$provinceName",
                                                            "receiverName": "测试",
                                                            "receiverMobile": "$mobile",
                                                            "receiveMobile": "$mobile",
                                                            "receiveAddress": "北京朝阳区三环以内测试",
                                                            "receiverAddress": "北京朝阳区三环以内测试",
                                                            "materialName": "测试"
                                                        })).call(studentCertificateApply)),
        Step(RunTestCase("申请列表,其他申请证明为审核中").with_variables(**({"a":"0","checkStatus":0})).call(getCertificateApply)),

        Step(RunTestCase("根据姓名查询 学员证明申请列表").setup_hook('${login_web()}', "Cookie").with_variables(**({"start":"0","length":"10","stdName":"$std_name"})).call(certificate_findAllList).export(*["certId","applyType","Cookie"])),
        Step(RunTestCase("审核学员证明为不通过").with_variables(**({"checkStatus":"-1","reason":"您申请的证明材料不在受理范围内","applyTyp":"$applyType"})).call(fdyCheck)),
        Step(RunTestCase("申请列表,其他申请证明为已驳回").with_variables(**({"a": "0", "checkStatus": -1})).call(getCertificateApply)),

    ]
if __name__ == '__main__':
    Test_Apply_qita().test_start()