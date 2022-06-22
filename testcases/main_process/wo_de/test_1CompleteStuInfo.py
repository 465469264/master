from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.operationStatistic import operationStatistic
from api.app.loginOrRegister import app_login
from api.app.getNeedCompleteStuInfo import getInvoiceApply
from api.app.stdLearnInfo import stdLearnInfo
from api.app.updateCompleteStuInfo import updateCompleteStuInfo
from api.app.getStsToken import getStsToken


class Test_perationStatistic(HttpRunner):
    config = (
        Config("完善成教资料")
            .verify(False)
            .variables(**{
            # "mobile": "${read_data_number(accountnumber,teacher_student6)}",
            "mobile": "15960652414",
            "localFile": "${read_data_number(SelClockTaskTopic_run,localFile)}",
            "bucketName": "yzimstemp",
        }
                       )
    )
    teststeps = [
        Step(RunTestCase("登录测试账号").call(app_login).export(*["app_auth_token", "userId", "realName"])),
        Step(RunTestCase("获取上传图片信息").call(getStsToken).teardown_hook('${upload($accessKeyId,$accessKeySecret,$endpoint,$localFile,$bucketName)}', "scPicUrl").export(*["scPicUrl"])),
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).export(*["scholarship","learnId", "mobile", "stdId","unvsId"])),

        Step(RunTestCase("获取需要完善的资料").call(getInvoiceApply).export(*["idCard", "stdId", "annexId0", "annexType0", "annexName0", "annexId1", "annexType1", "annexName1",
         "annexId2", "annexType2", "annexName2","annexId3", "annexType3", "annexName3","annexId4", "annexType4", "annexName4","annexId5", "annexType5", "annexName5",
         "birthday","stdName","jobType","isOpenUnvs","politicalStatus","isDataCheck","recruitType","sex","annexStatus"])),

        Step(RunTestCase("完善资料").with_variables(**({"nation":"01","now_province_name":"广东","rprAddressCode":"440101","graduateTime":"2018-02-23",
        "diploma":"123","edcsType":"1","profession":"无","now_district_name":"黄埔区","nowProvinceCode":"19","grade":"2022","now_city_name":"广州市","uploadType":0,"id_type":"1",
        "rprType":"1","address":"测试","unvsName":"测试","nowCityName":"广州市","uploadUser":"$stdName","nowCityCode":"1601","isDataCompleted":"0","maritalStatus":"1",
         "nowDistrictCode":"50283","uploadUserId":"$unvsId","annexUrl":"scPicUrl","nowDistrictName":"黄埔区","nowProvinceName":"广东"})).call(updateCompleteStuInfo)),

    ]


if __name__ == '__main__':
    Test_perationStatistic().test_start()
