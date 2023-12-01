#上进活动
from api.app.userHome import get_info
from httprunner import HttpRunner, Config, Step, RunTestCase
from api.app.selUpwardActivityInfo import selUpwardActivityInfo
from api.app.selUpwardActivityDetailById import selUpwardActivityDetailById
from api.app.addNewComment import AddNewComment
from api.app.usPraise import usPraise
from api.app.getCommentInfo import getCommentInfo
from api.app.DeleteComment import DeleteComment

class Test_Shang_Jin_Activity(HttpRunner):
    config = (
        Config("上进活动")
            .verify(False)
            .variables(**{
                            "type": "",           #不传时，获取所有    1>报名中  2>进行中   3>已结束
                            "picUrl": "",         #评论的图片-上传的配图路径
                            "targetUserId": "",   #回复的时候对应的 被回复人id
                            "ifLimit": "0",       #搜当前业务是否支持多次评论，0：支持，1 不支持索类型
                            "commentType": "3",    #评论业务 类型，1：咨询文章，2：上进故事 3：上进活动 4:圈子
                            "content": "${read_data_number(content_activity,content)}",     #写在data文件中的固定评论文案
                            "pageSize": "60",
                            "pageNum": 1,
                            "mappingType": "3",      #评论业务 类型，1：咨询文章，3：上进活动 4:圈子
                            "sortOrder": "",           #评论排序方式  1按热度  2按时间
                            "message":"success",
                            "msg": "请求成功",
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("APP获取个人信息").call(get_info).export(*["nickname", "realName", "userCircleRole", "stdName"])),
        Step(RunTestCase("活动列表").call(selUpwardActivityInfo).export(*["actId","actName"])),
        Step(RunTestCase("活动详情").call(selUpwardActivityDetailById).teardown_hook('${judge_fabulousNum($fabulous)}', "fabulousNum").export(*["fabulousNum"])),
        Step(RunTestCase("若用户活动没点赞，则点赞，否则取消点赞").with_variables(**({"fabulousNum": "$fabulousNum", "praiseId": "$actId", "praiseType": "2"})).call(usPraise)),
        Step(RunTestCase("对第一条帖子进行评论").with_variables(**({"circleUserId": "", "nickName": "$realName", "mappingId": "$actId",})).call(AddNewComment)),
        Step(RunTestCase("获取评论详情-提取出自己的评论id").with_variables(**({"mappingId": "$actId"})).call(getCommentInfo).teardown_hook('${get_comment_id($body,$realName)}', "comment_Id").export(*["comment_Id", "mappingId"])),
        Step(RunTestCase("删除自己评论，清理测试数据").call(DeleteComment)),

    ]

if __name__ == "__main__":
    Test_Shang_Jin_Activity().test_start()