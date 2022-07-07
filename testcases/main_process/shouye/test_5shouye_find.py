#首页-搜索
from httprunner import HttpRunner, Config, Step, Parameters, RunTestCase
from api.app.getSearchList import getSearchList

class Test_shouye_find(HttpRunner):
    config = (
        Config("搜索接口搜索不同类型")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "keyWords": "彭正",
                            "type": "7",
                            "pageNum": "1",
                             "pageSize": "20"
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("首页搜索-查找老师").call(getSearchList)),

    ]

if __name__ == "__main__":
    Test_shouye_find().test_start()



