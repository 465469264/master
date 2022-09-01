from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.web.zhimi_give_getUserInfo_do import getUserInfo
from api.web.livesAdmin_add_do import livesAdmin_add
from api.web.livesAdmin_list import livesAdmin_list
from api.web.livesAdmin_update import livesAdmin_update

class Test_lives_admin(HttpRunner):
    config = (
        Config("直播间管理员")
            .verify(False)
            .variables(**{
                        "mobile":"11223331848"           #随便创建管理员用到的手机号
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取用户信息，获取userId").setup_hook('${login_web()}', "Cookie").call(getUserInfo).export(*["user_id","yz_code","real_name","Cookie"])),
        Step(RunTestCase("新增房间管理员").with_variables(**({"userName":"$real_name","manageType": "1", "userId": "$user_id","yzCode": "$yz_code"})).call(livesAdmin_add)),
        Step(RunTestCase("获取管理员列表").call(livesAdmin_list).export(*["id"])),
        Step(RunTestCase("启用刚新增的管理员").with_variables(**({"isAllow": "1"})).call(livesAdmin_update)),
        Step(RunTestCase("禁用刚新增的管理员").with_variables(**({"isAllow": "2"})).call(livesAdmin_update)),
        Step(RunTestCase("然后在数据库删除垃圾数据，获取管理员列表").setup_hook('${delete_lives_admin($mobile)}').call(livesAdmin_list)),

    ]

if __name__ == '__main__':
    Test_lives_admin().test_start()