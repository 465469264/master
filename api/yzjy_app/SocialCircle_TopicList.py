#话题详情
from httprunner import HttpRunner, Config, Step, RunRequest
class SocialCircle_TopicList(HttpRunner):
    config = (
        Config("话题详情")
            .base_url("${ENV(yzjy-app)}")
            .verify(False)
            .variables(**{
                        "number": {
                            "data": {
                                    "pageNum": "$pageNum",
                                    "topicId": "$topicId",            #话题词详情
                                    "scType": "$scType",                   # #圈子类型    0  => 首页 1  => 同学圈 2  => 读书会 3  => 跑团圈 4  => 自考圈
                                                                #5  => 职业圈  6  => 关注  7  => 精选圈  8  => 精选圈-最新 9  => 精选圈-更多
                                                                #10 = > 话题词-话题详情  11 => 习惯-打卡记录 12 => 我的圈子  13 => 收藏列表
                                                                # 14 => 视频列表  #15 = > 读书笔记列表
                                    "pageSize": "$pageSize",
                                    },
                            "client": {
                                    "platform": "${ENV(platform)}",
                                    "appVersion": "${ENV(appVersion)}",
                                    "systemVersion": "${ENV(systemVersion)}"
                                        }
                                    }
                            }
                       )
                            )
    teststeps = [
        Step(
            RunRequest("话题详情")
                .post("/proxy/bbs-server/socialCircle/topicList/")
                .with_headers(**{
                "User-Agent": "${ENV(User-Agent)}",
                "appType": "${ENV(appType)}",
                "Content-Type": "application/json",
                "Accept-Encoding":"gzip, deflate, br",
                "Host": "${ENV(yzjy-app-Host)}",
                "authtoken": "${ENV(app_auth_token)}",
                                }
                              )
                .with_json("$number")
                .extract()
                .with_jmespath("body.data[0].id", "id")         #帖子id
                .validate()
                .assert_equal("body.state.msg", "$msg")

        )
    ]