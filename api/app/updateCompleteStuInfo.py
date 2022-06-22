from httprunner import HttpRunner, Config, Step, RunRequest
#完善资料
class updateCompleteStuInfo(HttpRunner):
    config = (
        Config("完善资料")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": {
                                    "body":{
                                        "nation": "$nation",                                 #民族
                                        "idCard": "$idCard",                                #身份证
                                        "now_province_name": "$now_province_name",          #户口所在地,枚举：广东
                                        "rprAddressCode": "$rprAddressCode",               #编码，所在地编码
                                        "rejectReason": [],
                                        "stdId": "$stdId",
                                        "graduateTime": "$graduateTime",                      #毕业时间
                                        "diploma": "$diploma",                                  #毕业编号
                                        "edcsType": "$edcsType",                                    #原学历类型：1>普通高中毕业，2>中专毕业，3>职业高中毕业....
                                        "profession": "$profession",                                #原毕业专业
                                        "now_district_name": "$now_district_name",                     #收教材地址
                                        "nowProvinceCode": "$nowProvinceCode",                              #收教材地址id
                                        "grade": "$grade",                                    #报考年级
                                        "annexInfos": "[{\"annexId\":\"$annexId0\",\"annexName\":\"$annexName0\",\"annexType\":\"$annexType0\",\"annexUrl\":\"$annexUrl\",\"isRequire\":\"1\",\"learnId\":\"$learnId\",\"updateTime\":\"\",\"uploadTime\":\"\",\"uploadUser\":\"$uploadUser\",\"uploadUserId\":\"$uploadUserId\"},{\"annexId\":\"$annexId1\",\"annexName\":\"$annexName1\",\"annexType\":\"$annexType1\",\"annexUrl\":\"$annexUrl\",\"isRequire\":\"1\",\"learnId\":\"$learnId\",\"updateTime\":\"\",\"uploadTime\":\"\",\"uploadUser\":\"$uploadUser\",\"uploadUserId\":\"$uploadUserId\"},{\"annexId\":\"$annexId2\",\"annexName\":\"$annexName2\",\"annexType\":\"$annexType2\",\"annexUrl\":\"$annexUrl\",\"isRequire\":\"1\",\"learnId\":\"$learnId\",\"updateTime\":\"\",\"uploadTime\":\"\",\"uploadUser\":\"$uploadUser\",\"uploadUserId\":\"$uploadUserId\"},{\"annexId\":\"$annexId3\",\"annexName\":\"$annexName3\",\"annexType\":\"$annexType3\",\"annexUrl\":\"annexUrl\",\"isRequire\":\"1\",\"learnId\":\"$learnId\",\"updateTime\":\"\",\"uploadTime\":\"\",\"uploadUser\":\"$uploadUser\",\"uploadUserId\":\"$uploadUserId\"},{\"annexId\":\"$annexId4\",\"annexName\":\"$annexName4\",\"annexType\":\"$annexType4\",\"annexUrl\":\"$annexUrl\",\"isRequire\":\"1\",\"learnId\":\"$learnId\",\"updateTime\":\"\",\"uploadTime\":\"\",\"uploadUser\":\"$uploadUser\",\"uploadUserId\":\"$uploadUserId\"},{\"annexId\":\"$annexId5\",\"annexName\":\"$annexName5\",\"annexType\":\"$annexType5\",\"annexUrl\":\"$annexUrl\",\"isRequire\":\"1\",\"learnId\":\"$learnId\",\"updateTime\":\"\",\"uploadTime\":\"\",\"uploadUser\":\"$uploadUser\",\"uploadUserId\":\"$uploadUserId\"}]",
                                        "now_city_name": "$now_city_name",                        #
                                        "stdName": "$stdName",                              #名称
                                        "uploadType": "$uploadType",                                #不知道啥字段
                                        "id_type": "$id_type",                                   #户口类型，1>农村户口，2>城镇户口，3>其他
                                        "rprType": "$rprType",                                  #不知道啥字段
                                        "address": "$address",                             #收教材详细地址
                                        "politicalStatus": "$politicalStatus",                       #不知道啥字段
                                        "sex": "$sex",                                           #性别
                                        "isOpenUnvs": "$isOpenUnvs",
                                        "unvsName": "$unvsName",                               #原毕业学校
                                        "isDataCheck": "$isDataCheck",
                                        "nowCityName":"$nowCityName",
                                        "learnId": "$learnId",
                                        "scholarship": "$scholarship",                               #优惠类型
                                        "annexList": [
                                            {
                                                "annexId": "$annexId0",
                                                "annexName": "$annexName0",
                                                "annexType": "$annexType0",
                                                "annexUrl": "$annexUrl",
                                                "isRequire": "1",
                                                "learnId": "$learnId",
                                                "uploadUser": "$uploadUser",
                                                "uploadUserId": "$uploadUserId"
                                            },
                                            {
                                                "annexId": "$$annexId1",
                                                "annexName": "$annexName1",
                                                "annexType": "$annexType1",
                                                "annexUrl": "$annexUrl",
                                                "isRequire": "1",
                                                "learnId": "$learnId",
                                                "uploadUser": "$uploadUser",
                                                "uploadUserId": "$uploadUserId"
                                            },
                                            {
                                                "annexId": "$annexId2",
                                                "annexName": "$annexName2",
                                                "annexType": "$annexType2",
                                                "annexUrl": "$annexUrl",
                                                "isRequire": "1",
                                                "learnId": "$learnId",
                                                "uploadUser": "$uploadUser",
                                                "uploadUserId": "$uploadUserId"
                                            },
                                            {
                                                "annexId": "$annexId3",
                                                "annexName": "$annexName3",
                                                "annexType": "$annexType3",
                                                "annexUrl": "$annexUrl",
                                                "isRequire": "1",
                                                "learnId": "$learnId",
                                                "uploadUser": "$uploadUser",
                                                "uploadUserId": "$uploadUserId"
                                            },
                                            {
                                                "annexId": "$annexId4",
                                                "annexName": "$annexName4",
                                                "annexType": "$annexType4",
                                                "annexUrl": "$annexUrl",
                                                "isRequire": "1",
                                                "learnId": "$learnId",
                                                "uploadUser": "$uploadUser",
                                                "uploadUserId": "$uploadUserId"
                                            },
                                            {
                                                "annexId": "$annexId5",
                                                "annexName": "$annexName5",
                                                "annexType": "$annexType5",
                                                "annexUrl": "$annexUrl",
                                                "isRequire": "1",
                                                "learnId": "$learnId",
                                                "uploadUser": "$uploadUser",
                                                "uploadUserId": "$uploadUserId"
                                            },
                                        ],
                                        "nowDistrictName":"$nowDistrictName",
                                        "isDataCompleted": "$isDataCompleted",
                                        "maritalStatus": "$maritalStatus",                            #婚姻状态
                                        "birthday": "$birthday",                        #生日
                                        "nowProvinceName":"$nowProvinceName",
                                        "jobType": "$jobType",                                  #职业
                                        "recruitType": "$recruitType",
                                        "mobile": "$mobile",
                                        "nowCityCode": "$nowCityCode",
                                        "nowDistrictCode": "$nowDistrictCode",
                                        "realName": "$realName",
                                        "annexStatus": "$annexStatus"
                                        },
                                        "header":{"appType":"3"}
                                    },
                          "data": "${base64_encode($number)}",
                          })
        )
    teststeps = [
        Step(
            RunRequest("完善资料")
                .post("/proxy/bds/updateCompleteStuInfo/1.0/")
                .with_headers(**{
                            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
                            "Content-Type": "base64.b64encode",
                            "Host": "${ENV(app_Host)}",
                            "authtoken": "$app_auth_token",

            }
            )
                .with_data('$data')
                .validate()
                .assert_equal("body.message", "success")
        )
    ]
if __name__ == '__main__':
    updateCompleteStuInfo().test_start()


