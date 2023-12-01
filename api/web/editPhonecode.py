from httprunner import HttpRunner, Config, Step, RunRequest
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class eddit_Phone_Message(HttpRunner):
    config = (
        Config("设置手机验证码")
            .base_url("${ENV(web_url)}")
            .verify(False)
            .variables(**{
                            "mobile": "${read_data_number(ApplyRecord,mobile)}",
                            }
                       )
        )
    teststeps = [
        Step(
            RunRequest("设置手机验证码")
                .get("/phoneCode/editPhonecode.do?phone=$mobile")
                .with_headers(**{
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                                    "uri": "http://test0-bms.yzwill.cn/toLogin.do",
                                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                    "Cookie": "COOKIE_USER_EMP=164629712848503561; _ga=GA1.2.827826091.1693790966; __gads=ID=7056769c4d935ee4-2220469165e300e6:T=1693790967:RT=1694082562:S=ALNI_MYxTcE6KW61OZMYET5SwF7TBSVKnw; __gpi=UID=00000c3b295015bc:T=1693790967:RT=1694082562:S=ALNI_MayP5tt2onklkem_DcbSZsXdrVW2w; SESSION=f3a134f5-93dd-4b50-8469-bb093a7d5320; acw_tc=0bca38ce16944991743574470e1ea205225a61de82b7a5e3d094217a85be9c; SERVERID=0b232a7dc2b0761157bd6b3a3b2b71ca|1694499257|1694499174"
                                }
                                )
                .extract()
                .validate()
                .assert_equal("body.body", "success")
        )
    ]
if __name__ == '__main__':
    eddit_Phone_Message().test_start()