from httprunner import HttpRunner, Config, Step, RunRequest
#运营>图片管理列表
class picture_list(HttpRunner):
    config = (
        Config("运营>图片管理列表")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("运营>图片管理列表")
                .post("/picture/list.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"$Cookie"
            })
                .with_data(
                            {
                            "isAllow":"$isAllow",                  #1>已启用
                            "picturePurpose":"$picturePurpose",        #日签>sign
                            "start": "0",
                            "length": "10"
                    }
                         )
                .extract()
                .with_jmespath("body.body.data[0].id","id")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
if __name__ == '__main__':
    picture_list().test_start()