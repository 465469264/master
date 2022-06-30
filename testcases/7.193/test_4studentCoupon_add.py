from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.loginOrRegister import app_login
from api.app.stdLearnInfo import stdLearnInfo
from api.web.loginByMobile_do import login_web
from api.web.studentCoupon_add import studentCoupon_add


class TestCasesenrollUpwardAct_sendAppMsg(HttpRunner):
    config = (
        Config("赠送优惠券给学员")
            .verify(False)
            .variables(**{"mobile": "${read_data_number(ApplyRecord,mobile)}",
                          "couponId":"${read_data_number(couponId,couponId)}"
                          })
            )
    teststeps = [
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).teardown_hook('${login_web()}', "Cookie").export(*["learnId","stdId","Cookie"])),
        Step(RunTestCase("赠送优惠券给学员").setup_hook('${coupon($couponId)}').with_variables(**({"remark":"测试","reasonDesc":"测试"})).call(studentCoupon_add)),

    ]
if __name__ == '__main__':
    TestCasesenrollUpwardAct_sendAppMsg().test_start()