#这期的需求--增加一个精选的圈子列表，取所有过往的热门帖子在这（不包含现在的热门帖子）   "dictName" : "精选", "dictValue" : "-1","dictName" : "最新",  "dictValue" : null,
# "scType": 读书社:scType.2,  跑团：scType.3，  自考圈：scType.4	，同学圈：scType.1   ，职场圈：scType.5
# "subType":普通贴：subType :0     1：读书贴  2：跑步贴）
from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.userHome import get_info
from api.app.usPostingApi import usPostingApi
from api.app.stdLearnInfo import stdLearnInfo

class Test_post_circle(HttpRunner):
    config = (
        Config("测试新的发帖接口")
            .verify(False)
            .variables(**{
                            "message": "success",
                            "scPicUrl":"",
                            "scText": "测试测试测试测试测试",
                            "scSource": "2"  # 帖子来源，1.安卓，2.iOS 3. 公众号 4.上进学社 5.红包
                        }
                       )
    )
    teststeps = [
        Step(RunTestCase('获取用户报读信息').call(stdLearnInfo).export(*["learnId1"])),
        Step(RunTestCase("发普通-读书社").with_variables(**({"learnId": "$learnId1","scType": "2","subType":"0"})).call(usPostingApi)),
        Step(RunTestCase("发普通-跑团").with_variables(**({"learnId": "$learnId1", "scType": "3", "subType": "0"})).call(usPostingApi)),
        Step(RunTestCase("发普通-职场圈").with_variables(**({"learnId": "$learnId1", "scType": "3", "subType": "0"})).call(usPostingApi)),
    ]
if __name__ == '__main__':
    Test_post_circle().test_start()