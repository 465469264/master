import pytest,sys,os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
print(str(Path(__file__).parent.parent.parent.parent))
from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.stdLearnInfo import stdLearnInfo
from api.web.studentCoupon_add import studentCoupon_add
from api.app.myCoupons import myCoupons

class TestCasesenrollUpwardAct_sendAppMsg(HttpRunner):
    @pytest.mark.parametrize("param",Parameters({"title-recruitType-scholarship-message":"${Coupons_scholarship()}"}))
    def test_start(self,param):
        super().test_start(param)
    config = (
        Config("赠送优惠券给学员")
            .verify(False)
            .variables(**{"mobile": "${read_data_number(ApplyRecord,mobile)}",
                          "couponId":"${read_data_number(couponId,couponId)}",
                            }
                       )
            )
    teststeps = [
        Step(RunTestCase("获取学员报读信息").call(stdLearnInfo).teardown_hook('${login_web()}', "Cookie").export(*["learnId","stdId","Cookie"])),
        Step(RunTestCase("赠送优惠券给学员").setup_hook('${coupon($couponId)}').with_variables(**({"remark":"测试","reasonDesc":"测试"})).call(studentCoupon_add)),
        Step(RunTestCase("查询所有优惠券").call(myCoupons)),
    ]
if __name__ == '__main__':
    TestCasesenrollUpwardAct_sendAppMsg().test_start()