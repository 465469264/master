from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.getCommentInfo import getCommentInfo
from api.app.userHome import get_info
from api.app.selCircleDynamicInfos import selCircleDynamicInfos2

class Test_reping(HttpRunner):
    config = (
        Config("热评 ")
            .verify(False)
            .variables(**{
            "userRoleType": 2,
            "own": 1,
            "pageSize": 20,
            "pageNum": 1
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("获取用户信息，获取userId").call(get_info).export(*["userId"])),
        Step(RunTestCase("查看自己的圈子").call(selCircleDynamicInfos2)),
        Step(RunTestCase("读书圈子评论-按时间排序,第一条评论是：嗨你好你好").with_variables(**({"mappingId": "67834","a":0,"sortOrder": "2","mappingType": "4","content":"嗨你好你好"})).call(getCommentInfo)),
        Step(RunTestCase("读书圈子评论-按热度排序,第二条评论是：我是热评，哈哈哈").with_variables(**({"mappingId": "67834","a": 0, "sortOrder": "1",  "mappingType": "4","content":"我是热评，哈哈哈"})).call(getCommentInfo)),


    ]

if __name__ == '__main__':
    Test_reping().test_start()