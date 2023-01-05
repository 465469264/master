from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.stdLearnInfo import stdLearnInfo
from api.app.userHome import get_info
from api.app.usNewPosting import usNewPosting
from api.app.getStsToken import getStsToken
from api.app.selCircleDynamicInfos import selCircleDynamicInfos2
from api.app.usSetDynamics import usSetDynamics
from api.app.selSocialCircleType import selSocialCircleType
from api.app.selRunInfo import selRunInfo


class Test_Read_habbit(HttpRunner):
    config = (
        Config("普通发帖")
            .verify(False)
            .variables(**{
                        "localFile": "${read_data_number(SelClockTaskTopic_run,localFile)}",
                        "bucketName": "yzimstemp",
                        "subType": "0",
                        "message": "success",
                        "own": "1",
                        "pageSize": 5,
                        "userRoleType": "",
                        "pageNum": 1,
                        "status": "3",  # 3>删除
                            }
                       )
             )
    teststeps = [
        Step(RunTestCase("登陆前，获取圈子的默认列表").call(selSocialCircleType)),
        Step(RunTestCase("获取账号的上进跑规则").call(selRunInfo)),
        Step(RunTestCase("获取登陆人参数").call(get_info).export(*["userId"])),
        Step(RunTestCase('获取用户报读信息').call(stdLearnInfo).export(*["learnId"])),
        Step(RunTestCase("获取上传图片信息").call(getStsToken).teardown_hook('${upload($accessKeyId,$accessKeySecret,$endpoint,$localFile,$bucketName)}', "scPicUrl").export(*["scPicUrl"])),
        Step(RunTestCase('发布帖子不带图片至读书社').with_variables(**({"scType": "2","scPicUrl": "","scText": "Amylee-自动发帖-不带图片-至读书社"})).call(usNewPosting)),
        Step(RunTestCase("进入自己的主页").call(selCircleDynamicInfos2).export(*["id"])),
        Step(RunTestCase("删除自己的第一条圈子").with_variables(**({"circleUserId": "$userId"})).call(usSetDynamics)),
        #
        Step(RunTestCase('发布帖子至读书社带图片').with_variables(**({"scType": "2", "scPicUrl": "$scPicUrl", "scText": "Amylee-自动发帖-带图片-至读书社"})).call(usNewPosting)),
        Step(RunTestCase("进入自己的主页").call(selCircleDynamicInfos2).export(*["id"])),
        Step(RunTestCase("删除自己的第一条圈子").with_variables(**({"circleUserId": "$userId"})).call(usSetDynamics)),

        Step(RunTestCase('发布帖子至跑团不带图片').with_variables(**({"scType": "3","scPicUrl": "", "scText": "Amylee-自动发帖-不带图片-至跑团"})).call(usNewPosting)),
        Step(RunTestCase("进入自己的主页").call(selCircleDynamicInfos2).export(*["id"])),
        Step(RunTestCase("删除自己的第一条圈子").with_variables(**({"circleUserId": "$userId"})).call(usSetDynamics)),

        Step(RunTestCase('发布帖子带图片至跑团').with_variables(**({"scType": "3","scPicUrl": "$scPicUrl", "scText": "Amylee-自动发帖-带图片-至跑团"})).call(usNewPosting)),
        Step(RunTestCase("进入自己的主页").call(selCircleDynamicInfos2).export(*["id"])),
        Step(RunTestCase("删除自己的第一条圈子").with_variables(**({"circleUserId": "$userId"})).call(usSetDynamics)),

        Step(RunTestCase('发布帖子至自考圈不带图片').with_variables(**({"scType": "4","scPicUrl": "", "scText": "Amylee-自动发帖-不带图片-至自考圈"})).call(usNewPosting)),
        Step(RunTestCase("进入自己的主页").call(selCircleDynamicInfos2).export(*["id"])),
        Step(RunTestCase("删除自己的第一条圈子").with_variables(**({"circleUserId": "$userId"})).call(usSetDynamics)),

        Step(RunTestCase('发布帖子带图片至自考圈').with_variables(**({"scType": "4","scPicUrl": "$scPicUrl", "scText": "Amylee-自动发帖-带图片-至自考圈"})).call(usNewPosting)),
        Step(RunTestCase("进入自己的主页").call(selCircleDynamicInfos2).export(*["id"])),
        Step(RunTestCase("删除自己的第一条圈子").with_variables(**({"circleUserId": "$userId"})).call(usSetDynamics)),

        Step(RunTestCase('发布帖子带图片至同学圈不带图片').with_variables(**({"scType": "1","scPicUrl": "", "scText": "Amylee-自动发帖-不带图片-至同学圈"})).call(usNewPosting)),
        Step(RunTestCase("进入自己的主页").call(selCircleDynamicInfos2).export(*["id"])),
        Step(RunTestCase("删除自己的第一条圈子").with_variables(**({"circleUserId": "$userId"})).call(usSetDynamics)),

        Step(RunTestCase('发布帖子带图片至同学圈').with_variables(**({"scType": "1","scPicUrl": "$scPicUrl", "scText": "Amylee-自动发帖-带图片-至同学圈"})).call(usNewPosting)),
        Step(RunTestCase("进入自己的主页").call(selCircleDynamicInfos2).export(*["id"])),
        Step(RunTestCase("删除自己的第一条圈子").with_variables(**({"circleUserId": "$userId"})).call(usSetDynamics)),
    ]
if __name__ == '__main__':
    Test_Read_habbit().test_start()