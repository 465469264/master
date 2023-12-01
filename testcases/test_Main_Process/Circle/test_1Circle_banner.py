#圈子列表-最新
from httprunner import HttpRunner, Config, Step, RunTestCase
from api.app.selCircleBannerList import selCircleBannerList
from api.app.usPraise import usPraise,usPraise2
from api.app.userHome import get_info
from api.app.addNewComment import AddNewComment
from api.yzjy_app.SocialCircle_CircleDetail import SocialCircle_CircleDetail_banner
from api.app.getCommentInfo import getCommentInfo
from api.app.DeleteComment import DeleteComment

class Test_Circle_Banner(HttpRunner):
    config = (
        Config("圈子bannaer的加载，进入，评论，点赞，生成海报")
            .verify(False)
            .variables(**{
                            "picUrl": "",         #评论的图片-上传的配图路径
                            "targetUserId": "",   #回复的时候对应的 被回复人id
                            "ifLimit": "0",       #搜当前业务是否支持多次评论，0：支持，1 不支持索类型
                            "commentType": "4",    #评论业务 类型，1：咨询文章，2：上进故事 3：上进活动 4:圈子
                            "content": "${read_data_number(content,content)}",     #写在data文件中的固定评论文案
                            "pageSize": "30",
                            "pageNum": 1,
                            "mappingType": "4",      #评论业务 类型，1：咨询文章，3：上进活动 4:圈子
                            "sortOrder": "1",           #评论排序方式  1按热度  2按时间
                            "message":"success",
                            "msg": "请求成功",
                            }
                       )
    )
    teststeps = [
        Step(RunTestCase("APP获取个人信息").call(get_info).export(*["nickname","realName","stdName"])),
        Step(RunTestCase("获取最新报读的轮播图").call(selCircleBannerList).export(*["mappingId","bannerId"])),
        Step(RunTestCase("圈子-banner进入帖子详情").with_variables(**({"id": "$mappingId"})).call(SocialCircle_CircleDetail_banner).teardown_hook('${judge_fabulousNum($fabulous)}',"fabulousNum").export(*["fabulousNum","userId"])),
        Step(RunTestCase("若用户还没在第一个轮播图点赞，则点赞，否则取消点赞").with_variables(**({"fabulousNum": "$fabulousNum","praiseId": "$mappingId","praiseType":"3"})).call(usPraise)),
        Step(RunTestCase("对轮播图的帖子进行评论").with_variables(**({"circleUserId": "$userId","nickName": "$realName"})).call(AddNewComment)),
        Step(RunTestCase("获取第一条轮播图的帖子评论详情").call(getCommentInfo).teardown_hook('${judge_ifFabulous($ifFabulous)}',"fabulousNum_recommend").export(*["commentId","fabulousNum_recommend"])),
        Step(RunTestCase("获取评论详情-提取出自己的评论id").call(getCommentInfo).teardown_hook('${get_comment_id($body,$realName)}', "comment_Id").export(*["comment_Id"])),
        Step(RunTestCase("删除自己评论，清理测试数据").setup_hook('${edit_photo(跑步上传.jpg)}').call(DeleteComment)),



    ]

if __name__ == "__main__":
    Test_Circle_Banner().test_start()