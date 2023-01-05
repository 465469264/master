from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.web.picture_list import picture_list
from api.web.picture_edit import picture_edit
from api.app.getSignInfo import getSignInfo

class edit_photo(HttpRunner):
    config = (
        Config("自考延长考期跟进")
            .verify(False)
            .variables(**{
                            "isAllow": "1",         #已启用
                            "picturePurpose": "sign",    #的日签
                            "Cookie":"SESSION=6a023c6a-b7cc-44d1-ab39-a444c92a5e22",
                            "exType": "UPDATE",
                            "pictureName":"测试",
                            "sharePictureType":"1",
                            "appPic":"",
                            "appPic:pictureUrl":"appSharePic/测试图片.png",
                            "isPhotoChange":"",
                            "sort": "0",                    #排序为0
                            "pictureDesc":"测试",
                            "picToUrl":"www.baidu.com",
                            "message": "success",
                                    }
                       )
    )
    teststeps = [
        #此用例在于签到接口--获取到后台配置的图片跳转链接，用于点击图片进行跳转
        Step(RunTestCase("获取已启用的日签").call(picture_list).export(*["id"])),
        Step(RunTestCase("修改日签").call(picture_edit)),
        Step(RunTestCase("获取签到信息--获取到这个签到图片的跳转url").call(getSignInfo)),

    ]

if __name__ == '__main__':
    edit_photo().test_start()