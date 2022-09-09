from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.web.zkDefer_getList import zkDefer_getList
from api.web.zkDefer_getDelayRecord import zkDefer_getDelayRecord
from api.web.zkDefer_getApplyDelayInfo import zkDefer_getApplyDelayInfo
from api.web.zkDefer_applyDelay import zkDefer_applyDelay

class Test_zkDefer(HttpRunner):
    config = (
        Config("自考延长考期跟进")
            .verify(False)
            .variables(**{
                            "stdName": "李翠莹",
                            "ifApplyDelay": ""
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取自考延长考期跟进列表").setup_hook('${login_web()}', "Cookie").with_variables(**({"stdName": "","ifApplyDelay": ""})).call(zkDefer_getList).export(*["Cookie"])),
        Step(RunTestCase("获取自考延长考期跟进列表-根据筛选条件名字查询").call(zkDefer_getList).export(*["learnId"])),
        Step(RunTestCase("自考延长考期跟进------查看延期记录").call(zkDefer_getDelayRecord)),
        Step(RunTestCase("自考延长考期跟进------获取延期申请信息").call(zkDefer_getApplyDelayInfo).export(*["serviceTimeEnd"])),
        Step(RunTestCase("自考延长考期跟进------老师操作延期").with_variables(**({"applyServiceTimeEnd": "$serviceTimeEnd"})).call(zkDefer_applyDelay))

    ]

if __name__ == '__main__':
    Test_zkDefer().test_start()