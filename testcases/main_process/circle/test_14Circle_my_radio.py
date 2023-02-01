#圈子页-我的视频
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from api.app.userHome import get_info
from api.app.selCircleVideoInfo import selCircleVideoInfo
from api.app.usDataRecord import usDataRecord



class TestCaseCircle_My_video(HttpRunner):
    config = (
        Config("圈子页-读书记录")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "unit": "3",            # 单位 : 1/次数 2/分钟 3/秒
                            "onlineDuration": "7",  # 时长
                            "businessType": "6",    #：课程资料 2：复习资料 3：直播 4：录播 5：回放 6：短视频 7：直播广场直播 8：直播广场录播 9：直播广场回放
                            "eventType": "2",        #eventType   1：下载 2：视频时长
                            "pageSize": "20",
                            "pageNum": "1",
                            "userRoleType":"2"
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取用户信息，获取userId").call(get_info).export(*["userId","ruleType"])),
        Step(RunTestCase('圈子页-我的视频').call(selCircleVideoInfo).export(*["id"])),
        Step(RunTestCase('视频播放后-进行埋点').with_variables(**({"mappingId":"$id"})).call(usDataRecord)),

    ]

if __name__ == "__main__":
    TestCaseCircle_My_video().test_start()

