from httprunner import HttpRunner, Config, Step, RunRequest
#查询考前辅导费缴费列表
class picture_edit(HttpRunner):
    config = (
        Config("运营-图片管理")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("运营-图片管理")
                .post("/picture/edit.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"$Cookie"
            })
                .with_data({
                    "exType": "$exType",               #UPDATE>更新
                    "id": "$id",                        #图片的id
                    "pictureName": "$pictureName",            #图片名字
                    "picturePurpose":"$picturePurpose",            #sign>日签
                    "sharePictureType":"$sharePictureType",           #类型
                    "appPic":"$appPic",                      #没做修改时，传空
                    "pictureUrl":"appSharePic/测试图片.png",      #图片地址
                    "isPhotoChange":"",                     #不修改图片时传空
                    "pictureDesc": "测试",                   #描述
                    "sort": "$sort",                       #排序
                    "picToUrl": "$picToUrl"            #修改链接

                    }
            )
                .extract()
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    picture_edit().test_start()