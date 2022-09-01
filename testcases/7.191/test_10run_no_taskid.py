from httprunner import HttpRunner, Config, Step, Parameters,RunTestCase
from api.app.stdLearnInfo import stdLearnInfo
from api.app.selClockTaskTopic import SelClockTaskTopic
from api.app.getStsToken import getStsToken
from api.app.usRunningExt import usRunningExt
from api.app.selCircleDynamicInfos import selCircleDynamicInfos
from api.app.userHome import get_info


class test_10run_no_taskid(HttpRunner):
    config = (
                Config("跑步打卡传值不传taskid,同时多次打卡")
                    .verify(False)
                    .variables(**{
                    "localFile": "${read_data_number(SelClockTaskTopic_run,localFile)}",
                    "bucketName": "yzimstemp",
                    "message": "success",

                                }
                       )
            )
    teststeps = [
        Step(RunTestCase("获取上传图片信息").call(getStsToken).teardown_hook('${upload($accessKeyId,$accessKeySecret,$endpoint,$localFile,$bucketName)}', "scPicUrl").export(*["scPicUrl"])),
        # Step(RunTestCase("发贴跑步习惯打卡帖子").call(usRunningExt)),
    ]

if __name__ == '__main__':
    test_10run_no_taskid().test_start()