#圈子-动态页加载branner
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.selCircleBannerList import selCircleBannerList
from api.app.selCircleTopic import selCircleTopic
from api.web.toBannerEdit import toBannerEdit_webtoken
from api.web.circleDynamic_bannerEdit import circleDynamic_bannerEdit
from api.app.selCommonMarketMenu import selCommonMarketMenu

class Test_BannerList(HttpRunner):
    config = (
        Config("习惯打卡里的接口")
            .verify(False)
            .variables(**{
            "pageSize": "10",
            "pageNum": "1",
            "type": "",
            "bannerId": "158691751551831152",
            "historyNum": 0,
            "appBannerType": "sq_10",
            "sort": "23",
            "bannerUrl": "banner/158691751551831152/8C7F0041464B4DCAAC6D5ADAB922B47C.jpeg",
            "bannerName": "圣诞快乐测试",
            "bannerDesc":"圣诞快乐测试",
            "message": "success"

        })
    )
    teststeps = [
        Step(RunTestCase("获取修改branner的webtoken").setup_hook('${login_web()}', "Cookie").call(toBannerEdit_webtoken).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token","Cookie"])),
        Step(RunTestCase("学员系统修改branner的名字").call(circleDynamic_bannerEdit)),
        Step(RunTestCase("动态页加载branner").call(selCircleBannerList)),
        Step(RunTestCase("返回话题").call(selCircleTopic)),
        Step(RunTestCase("首页的菜单").with_variables(**({"level": "2","menuType": "1"})).call(selCommonMarketMenu)),
        Step(RunTestCase("学堂页的菜单").with_variables(**({"level": "2", "menuType": "2"})).call(selCommonMarketMenu)),
        Step(RunTestCase("发现页的菜单").with_variables(**({"level": "2", "menuType": "3"})).call(selCommonMarketMenu)),
        Step(RunTestCase("我的页面的菜单").with_variables(**({"level": "2", "menuType": "4"})).call(selCommonMarketMenu)),

    ]

if __name__ == "__main__":
    Test_BannerList().test_start()



