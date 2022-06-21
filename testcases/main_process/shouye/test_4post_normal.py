from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.loginOrRegister import app_login
from api.app.stdLearnInfo import stdLearnInfo
from api.app.usNewPosting import usNewPosting
from api.app.getStsToken import getStsToken


class Test_Read_habbit(HttpRunner):
    config = (
        Config("普通发帖")
            .verify(False)
            .variables(**{
            "mobile": "${read_data_number(accountnumber,teacher_student6)}",
            "localFile": "${read_data_number(SelClockTaskTopic_run,localFile)}",
            "bucketName": "yzimstemp",

                        }
                       )
    )
    teststeps = [
        Step(RunTestCase("登录测试账号").call(app_login).export(*["app_auth_token","userId"])),
        Step(RunTestCase('获取用户报读信息').call(stdLearnInfo).export(*["learnId","pfsnName"])),
        Step(RunTestCase("获取上传图片信息").call(getStsToken).teardown_hook('${upload($accessKeyId,$accessKeySecret,$endpoint,$localFile,$bucketName)}', "scPicUrl").export(*["scPicUrl"])),
        Step(RunTestCase('发布帖子至读书社').with_variables(**({"scType": "2","subType": "0","scPicUrl": "","scText": "Amylee-自动发帖-不带图片-至读书社"})).call(usNewPosting)),
        # Step(RunTestCase('发布帖子至读书社').with_variables(**({"scType": "2", "subType": "0", "scPicUrl": "$scPicUrl", "scText": "Amylee-自动发帖-带图片-至读书社"})).call(usNewPosting)),
        # Step(RunTestCase('发布帖子至跑团').with_variables(**({"scType": "3", "subType": "0", "scPicUrl": "", "scText": "Amylee-自动发帖-不带图片-至跑团"})).call(usNewPosting)),
        # Step(RunTestCase('发布帖子至跑团').with_variables(**({"scType": "3", "subType": "0", "scPicUrl": "$scPicUrl", "scText": "Amylee-自动发帖-带图片-至跑团"})).call(usNewPosting)),
        # Step(RunTestCase('发布帖子至自考圈').with_variables(**({"scType": "4", "subType": "0", "scPicUrl": "", "scText": "Amylee-自动发帖-不带图片-至自考圈"})).call(usNewPosting)),
        # Step(RunTestCase('发布帖子至自考圈').with_variables(**({"scType": "4", "subType": "0", "scPicUrl": "$scPicUrl", "scText": "Amylee-自动发帖-带图片-至自考圈"})).call(usNewPosting)),
        # Step(RunTestCase('发布帖子至同学圈').with_variables(**({"scType": "1", "subType": "0", "scPicUrl": "", "scText": "Amylee-自动发帖-不带图片-至同学圈"})).call(usNewPosting)),
        # Step(RunTestCase('发布帖子至同学圈').with_variables(**({"scType": "1", "subType": "0", "scPicUrl": "$scPicUrl", "scText": "Amylee-自动发帖-带图片-至同学圈"})).call(usNewPosting)),
    ]
if __name__ == '__main__':
    Test_Read_habbit().test_start()