from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.loginOrRegister import app_login
from api.app.getCommentInfo import getCommentInfo

class Test_reping(HttpRunner):
    config = (
        Config("热评 ")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(accountnumber,teacher_student6)}",

                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("登录测试账号").call(app_login).export(*["app_auth_token","userId"])),
        Step(RunTestCase("读书圈子评论-按时间排序,第一条评论是：嗨你好你好").with_variables(**({"mappingId": "67834","a":0,"pageSize": "15","sortOrder": "2","pageNum": 1,"mappingType": "4","content":"嗨你好你好"})).call(getCommentInfo)),
        Step(RunTestCase("读书圈子评论-按热度排序,第二条评论是：我是热评，哈哈哈").with_variables(**({"mappingId": "67834","a": 0, "pageSize": "15", "sortOrder": "1", "pageNum": 1, "mappingType": "4","content":"我是热评，哈哈哈"})).call(getCommentInfo)),


    ]

if __name__ == '__main__':
    Test_reping().test_start()