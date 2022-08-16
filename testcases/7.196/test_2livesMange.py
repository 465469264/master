from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.web.livesManage_list import livesManage_list


class Test_lives_admin(HttpRunner):
    config = (
        Config("直播列表")
            .verify(False)
            .variables(**{
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("后台-直播列表").setup_hook('${login_web()}', "Cookie").call(livesManage_list)),
        

    ]

if __name__ == '__main__':
    Test_lives_admin().test_start()