#圈子-读书会
from httprunner import HttpRunner, Config, Step, RunTestCase
from api.yzjy_app.SocialCircle_list import SocialCircle_list
from api.yzjy_app.SocialCircle_CircleDetail import SocialCircle_CircleDetail
from api.app.addNewComment import AddNewComment
from api.app.userHome import get_info
from api.app.usPraise import usPraise
from api.app.selPraiseList import SelPraiseList
from api.app.Invite_GetInvitationQRCode import Iinvite_GetInvitationQRCode
from api.app.getCommentInfo import getCommentInfo
from api.app.DeleteComment import DeleteComment

class Test_Circle_List_Read(HttpRunner):
    config = (
        Config("圈子-读书会列表，进入，评论，点赞，生成海报")
            .verify(False)
            .variables(**{
                            "mappingType": "4",  # 评论业务 类型，1：咨询文章，2：上进活动 4:圈子
                            "sortOrder": "1",  # 评论排序方式  1按热度  2按时间
                            "picUrl": "",  # 评论的图片-上传的配图路径
                            "targetUserId": "",  # 回复的时候对应的 被回复人id
                            "ifLimit": "0",  # 搜当前业务是否支持多次评论，0：支持，1 不支持索类型
                            "commentType": "4",  # 评论业务 类型，1：咨询文章，2：上进故事 3：上进活动 4:圈子
                            "content": "${read_data_number(content,content)}",  # 写在data文件中的固定评论文案
                            "pageNum": 1,
                            "pageSize": 20,
                            "page":"pages/other/news/index",               #小程序路径
                            "message":"success",
                            "msg": "请求成功",
                            "scType": "2"              #2  => 读书会
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("APP获取个人信息").call(get_info).export(*["nickname","realName","userCircleRole","stdName"])),
        Step(RunTestCase("查看圈子列表-精选更多-提取第一条帖子id").with_variables(**({"userRoleType": "$userCircleRole"})).call(SocialCircle_list).export(*["id"])),
        Step(RunTestCase("精选-更多列表进入帖子详情").call(SocialCircle_CircleDetail).teardown_hook('${judge_fabulousNum($fabulous)}', "fabulousNum").export(*["fabulousNum", "userId"])),
        Step(RunTestCase("帖子的点赞列表").call(SelPraiseList)),
        Step(RunTestCase("若用户还没在第一个帖子点赞，则点赞，否则取消点赞").with_variables(**({"fabulousNum": "$fabulousNum", "praiseId": "$id", "praiseType": "3"})).call(usPraise)),
        Step(RunTestCase("对第一条帖子进行评论").with_variables(**({"circleUserId": "$userId", "nickName": "$realName","mappingId": "$id"})).call(AddNewComment)),
        Step(RunTestCase("获取评论详情-提取出自己的评论id").with_variables(**({"mappingId": "$id"})).call(getCommentInfo).teardown_hook('${get_comment_id($body,$realName)}', "comment_Id").export(*["comment_Id", "mappingId"])),
        Step(RunTestCase("删除自己评论，清理测试数据").call(DeleteComment)),
        Step(RunTestCase("生成邀约帖子的海报").with_variables(**({"circleId":"$id","regOrigin":"1"})).call(Iinvite_GetInvitationQRCode)),

    ]

if __name__ == "__main__":
    Test_Circle_List_Read().test_start()