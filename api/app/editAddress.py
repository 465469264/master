from httprunner import HttpRunner, Config, Step, RunRequest
#购物添加收获地址
class eddit_address(HttpRunner):
    config = (
        Config("收货地址")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "saName": "$saName",                     #收货人
                                            "address": "$address",                  #详细地址
                                            "districtCode": "$districtCode",        #区的编码
                                            "districtName": "$districtName",        #区名称
                                            "cityCode": "$cityCode",                  #市编码
                                            "cityName": "$cityName",                # 市名,
                                            "provinceCode": "$provinceCode",        #省编码
                                            "provinceName": "$provinceName",        # 省份名字
                                            "streetName": "$streetName",            #街道名
                                            "streetCode": "$streetCode",            #街道码
                                            "mobile": "$mobile",                    #手机号码
                                            "isDefault": "2",                    #未知字段
                                            "saType": "$saType",                   #地址类型	  1>教材地址	  2>试卷邮寄地址	  3>收获地址
                                            "saId":"$saId",                       #编辑地址需要有地址id，从我的地址这个接口获取

                                            "excType": "$excType",                   #1>新增   2> 保存
                                            "email": "$email"                 #邮箱
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
            RunRequest("收获地址")
                .post("/proxy/us/editAddress/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.19.9/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "frontTrace": "{\"transferSeq\":\"1\",\"phoneModel\":\"SM-N9500\",\"app_type\":\"android\",\"app_version\":\"7.19.9\",\"title\":\"getCertificateApply\",\"transferId\":\"165596882382164439\",\"uri\":\"/proxy/bds/getCertificateApply/1.0/\",\"phoneSys\":\"9\",\"app_sdk\":\"28\",\"sendTime\":\"1655968823822\"}",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .validate()
                .assert_equal("status_code", 200)
        )
    ]