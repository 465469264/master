from httprunner import HttpRunner, Config, Step, RunRequest
#申请报读证明
class studentCertificateApply(HttpRunner):
    config = (
        Config("申请证明")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            #这些时申请“其他”时的必传字段
                                            "districtCode": "$districtCode",         #区的编码
                                            "district": "$district",                  #区名
                                            "city": "$city",                        #市名
                                            "cityCode": "$cityCode",              #市编码
                                            "street": "$street",                          # 县
                                            "provinceCode": "$provinceCode",        # 省编码
                                            "province": "$province",                # 省名
                                            "receiveName": "$receiveName",        #收获人名字
                                            "stampDown": "$stampDown",             # 未知字段   传1

                                            "receiverName": "$receiverName",       #收货人名字
                                            "receiverMobile": "$receiverMobile",  #收获人手机号码
                                            "receiveMobile": "$receiveMobile",   #收获人手机号码
                                            "receiveAddress": "$receiveAddress",        #收获地址
                                            "receiverAddress": "$receiverAddress",        #收货人地址
                                            "materialName":"$materialName",             #材料名称

                                            #公用字段
                                            "applyType": "$applyType",        # 6>报读证明  5>其他       3>查询
                                            "remark": "$remark",                #备注
                                            "stdName": "$stdName",
                                            "receiveType": "$receiveType",             # 收获类型1>快递
                                            "unvsName": "$unvsName",
                                            "userId": "$userId",
                                            "applyPurpose": "$applyPurpose",            #申请理由
                                            "grade": "$grade",
                                            "learnId": "$learnId"
                                            },
                                    "header":{
                                        "appType":"3"
                                    }
                                },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("申请证明")
                .post("/proxy/bds/studentCertificateApply/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "frontTrace": "{\"transferSeq\":\"1\",\"phoneModel\":\"SM-N9500\",\"app_type\":\"android\",\"app_version\":\"7.19.9\",\"title\":\"getCertificateApply\",\"transferId\":\"165596882382164439\",\"uri\":\"/proxy/bds/getCertificateApply/1.0/\",\"phoneSys\":\"9\",\"app_sdk\":\"28\",\"sendTime\":\"1655968823822\"}",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]
if __name__ == '__main__':
    studentCertificateApply().test_start()

#申请报读证明
class studentCertificateApply2(HttpRunner):
    config = (
        Config("申请证明")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "applyType": "$applyType",  # 6>报读证明  5>其他       3>查询
                                            "remark": "$remark",                        #备注
                                            "stdName": "$stdName",
                                            "receiveType": "$receiveType",             #未知字段
                                            "unvsName": "$unvsName",
                                            "userId": "$userId",
                                            "applyPurpose": "$applyPurpose",            #申请理由
                                            "grade": "$grade",
                                            "learnId": "$learnId"
                                            },
                                    "header":{
                                        "appType":"3"
                                    }
                                },
                            "data": "${base64_encode($number)}"
                        })
            )
    teststeps = [
        Step(
            RunRequest("申请证明")
                .post("/proxy/bds/studentCertificateApply/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "frontTrace": "{\"transferSeq\":\"1\",\"phoneModel\":\"SM-N9500\",\"app_type\":\"android\",\"app_version\":\"7.19.9\",\"title\":\"getCertificateApply\",\"transferId\":\"165596882382164439\",\"uri\":\"/proxy/bds/getCertificateApply/1.0/\",\"phoneSys\":\"9\",\"app_sdk\":\"28\",\"sendTime\":\"1655968823822\"}",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .extract()
                .validate()
                .assert_equal("body.message", "$message")
        )
    ]