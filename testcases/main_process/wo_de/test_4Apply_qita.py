from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.getJDTown import getJDTown
from api.app.stdLearnInfo import stdLearnInfo
from api.app.studentCertificateApply import studentCertificateApply
from api.app.getJDProvince import GetJDProvince
from api.app.getJDCity import getJDCity
from api.app.getJDCounty import getJDCounty
from api.app.editAddress import eddit_address
from api.app.myAddress import myAddress
from api.app.getCertificateApply import getCertificateApply
from api.web.certificate_findAllList import certificate_findAllList
from api.web.certificate_fdyCheck import fdyCheck
from api.app.userHome import get_info

class Test_Apply_qita(HttpRunner):
    config = (
        Config("申请其他证明")
            .verify(False)
            .variables(**{
                "mobile": "${read_data_number(ApplyRecord,mobile)}",
                "applyType": "5",   #申报类型为”其他“
                "remark": "测试",
                "applyPurpose": "测试",
                "receiveType": "1",
                "message": "success",
                 "stampDown": "1",
                })
    )
    teststeps = [
        Step(RunTestCase("获取信息").call(get_info).export(*["userId","stdName"])),
        Step(RunTestCase("获取我的地址").with_variables(**({"saType": "3"})).call(myAddress).export(*["saId"])),
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["learnId","grade"])),
        Step(RunTestCase("获取省份").call(GetJDProvince).export(*["provinceCode", "provinceName"])),
        Step(RunTestCase("获取城市").with_variables(**({"id": "$provinceCode"})).call(getJDCity).export(*["cityCode", "cityName"])),
        Step(RunTestCase("地区").with_variables(**({"id": "$cityCode"})).call(getJDCounty).export(*["districtCode", "districtName"])),
        Step(RunTestCase("乡镇").with_variables(**({"id": "$districtCode"})).call(getJDTown).export(*["streetCode", "streetName"])),
        Step(RunTestCase("编辑收货地址").with_variables(**({"saName": "测试", "address": "测试地址", "saType": "3", "excType": "2", "email": "123@qq.com"})).call(eddit_address)),
        Step(RunTestCase("我的地址").with_variables(**({"saType": "3"})).call(myAddress).export(*["districtCode","districtName","provinceCode","provinceName","cityName","cityCode","streetName","address"])),

        Step(RunTestCase("申请其他证明").with_variables(**({
                                                            "districtCode": "$districtCode",            #区的编码
                                                            "district": "$districtName",                     # 区名
                                                            "city": "$cityName",                            # 市名
                                                            "cityCode": "$cityCode",                   # 市编码
                                                            "street": "$streetName",                       # 县
                                                            "provinceCode": "$provinceCode",           # 省编码
                                                            "province": "$provinceName",                  # 省名
                                                            "receiverName": "测试",
                                                            "receiveName": "测试",
                                                            "receiverMobile": "$mobile",
                                                            "receiveMobile": "$mobile",
                                                            "receiveAddress": "$provinceName"+"$cityName"+"$districtName"+"$streetName"+"$address",
                                                            "receiverAddress": "$provinceName"+"$cityName"+"$districtName"+"$streetName"+"$address",
                                                            "unvsName": "",
                                                            "materialName": "测试"
                                                        })).call(studentCertificateApply)),

        Step(RunTestCase("申请列表,其他申请证明为审核中").with_variables(**({"a":"0","checkStatus":0})).call(getCertificateApply)),

        Step(RunTestCase("根据姓名查询 学员证明申请列表").setup_hook('${login_web()}', "Cookie").with_variables(**({"start":"0","length":"10"})).call(certificate_findAllList).export(*["certId","applyType","Cookie"])),
        Step(RunTestCase("审核学员证明为不通过").with_variables(**({"checkStatus":"-1","reason":"您申请的证明材料不在受理范围内","applyTyp":"$applyType"})).call(fdyCheck)),
        Step(RunTestCase("申请列表,其他申请证明为已驳回").with_variables(**({"a": "0", "checkStatus": -1})).call(getCertificateApply)),

    ]
if __name__ == '__main__':
    Test_Apply_qita().test_start()