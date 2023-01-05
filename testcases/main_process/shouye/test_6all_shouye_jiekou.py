from httprunner import HttpRunner, Config, Step, Parameters, RunTestCase
from api.app.getSystemDateTime import getSystemDateTime
from api.app.selAppHotAct import selAppHotAct
from api.app.selAppGoodsShop import selAppGoodsShop
from api.app.selAppAdvertisement import selAppAdvertisement
from api.app.getAPPVersionInfo import getAPPVersionInfo
from api.app.scholarshipStoryList import scholarshipStoryList
from api.app.userHome import get_info
from api.app.selAppPostingInfos import selAppPostingInfos
from api.app.getAppSettings import getAppSettings
from api.app.selAppHpMarketMenu import selAppHpMarketMenu

class Test_shouye_jiekou(HttpRunner):
    config = (
        Config("首页的接口")
            .verify(False)
            .variables(**{
                            "level": "2",
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
        Step(RunTestCase("获取用户信息，获取userId").setup_hook('${delay(1)}').call(get_info).export(*["userId"])),
        Step(RunTestCase("根据app版本号获取app设置").call(getAppSettings)),
        Step(RunTestCase("获取系统时间").call(getSystemDateTime)),
        Step(RunTestCase("首页热门活动").call(selAppHotAct)),
        Step(RunTestCase("首页-商品").call(selAppGoodsShop)),
        Step(RunTestCase("首页-弹窗广告").call(selAppAdvertisement)),
        # Step(RunTestCase("获取APP版本信息").call(getAPPVersionInfo)),           #这个接口，在27环境经常会挂
        Step(RunTestCase("获取上进故事").call(scholarshipStoryList)),
        Step(RunTestCase("首页金刚区菜单").call(selAppHpMarketMenu)),
        Step(RunTestCase("首页不知道什么接口---接口文档找不到").call(selAppPostingInfos)),
    ]

if __name__ == "__main__":
    Test_shouye_jiekou().test_start()



