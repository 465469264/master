from httprunner import HttpRunner, Config, Step, Parameters, RunTestCase
from api.app.getSystemDateTime import getSystemDateTime
from api.app.selAppHotAct import selAppHotAct
from api.app.selAppGoodsShop import selAppGoodsShop
from api.app.selAppAdvertisement import selAppAdvertisement
from api.app.getAPPVersionInfo import getAPPVersionInfo


class Test_shouye_jiekou(HttpRunner):
    config = (
        Config("首页的接口")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "menuType": "1",              #1>首页
                            "pageSize": "4",             # 1>显示一个，2>显示两个
                            "pageNum": "1",
                            "salesType": "1",           # 1>兑换活动  2>抽奖活动  3>竞价活动  4>生日活动
                            "goodsType": "1",            # 1>普通商品	 2>课程商品	3>活动商品	4>教材商品	 5>生日商品
                            "adFirstType": "1",          #1广告  2启动页
                            "activityName" :"我是amylee"
    }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取系统时间").call(getSystemDateTime)),
        Step(RunTestCase("首页热门活动").call(selAppHotAct)),
        Step(RunTestCase("首页-商品").call(selAppGoodsShop)),
        Step(RunTestCase("首页-弹窗广告").call(selAppAdvertisement)),
        Step(RunTestCase("获取APP版本信息").call(getAPPVersionInfo)),

    ]

if __name__ == "__main__":
    Test_shouye_jiekou().test_start()



