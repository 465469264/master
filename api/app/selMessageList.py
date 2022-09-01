from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
#进入直播间----获取直播间的消息列表
class selMessageList(HttpRunner):
    config = (
        Config("进入直播间----获取直播间的消息列表")
            .base_url("${ENV(im)}")
            .verify(False)
            .variables(**{
                            }
                       )
    )
    teststeps = [
        Step(
            RunRequest("进入直播间----获取直播间的消息列表")
            .post("/proxy/im-msg/message/selMessageList")
            .with_headers(
                **{
                    "User-Agent": "yuan zhi jiao yu/7.19.6 (iPhone; iOS 12.5.5; Scale/3.00)",
                    "Content-Type": "application/json",
                    "Host":"${ENV(im_host)}",
                    "Connection":"Keep-Alive"
                }
            )
            .with_json(
                         {
                            "groupId": "$groupId",
                            "sort": "$sort",                         #1：升序 2：降序 不传默认不排序
                            "pageSize": "50",
                            "pageNum": "1"
                            }
                        )
            .extract()
            .validate()
            .assert_equal("body.message", "$message")
        ),
    ]