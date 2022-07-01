#后台创建商品
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.web.goodsUpdate import goodsUpdate
class Test_goodsUpdate(HttpRunner):
    config = (
        Config("后台创建商品")
            .verify(False)
            .variables(**{
        })
    )
    teststeps = [
        Step(RunTestCase("后台创建商品").setup_hook('${login_web()}', "Cookie").call(goodsUpdate))
    ]

if __name__ == "__main__":
    Test_goodsUpdate().test_start()



