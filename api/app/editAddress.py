from httprunner import HttpRunner, Config, Step, RunRequest
#购物添加收获地址
class eddit_address(HttpRunner):
    config = (
        Config("购物添加收获地址")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                            "number": {
                                    "body":{
                                            "saName": "$saName",                   #收货人
                                            "address": "$address",                  #详细地址
                                            "districtCode": "$districtCode",     #区的编码
                                            "districtName": "$districtName",     #区名称
                                            "cityCode": "$cityCode",                  #市编码
                                            "provinceCode": "$provinceCode",                #省编码
                                            "mobile": "$mobile",             #手机号码
                                            "cityName": "$cityName",             #市名,
                                            "isDefault": "2",
                                            "saType": "$saType",                   #地址类型	  1>教材地址	  2>试卷邮寄地址	  3>收获地址
                                            "CREATOR": {},
                                            "provinceName": "$provinceName",           #省份名字
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
            RunRequest("添加收获地址")
                .post("/proxy/us/editAddress/1.0/")
                .with_headers(**{
                "Accept - Encoding": "gzip",
                "User-Agent": "Android/environment=test/app_version=7.19.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                "Host": "${ENV(app_Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                            })
                .with_data('$data')
                .validate()
                .assert_equal("status_code", 200)
        )
    ]