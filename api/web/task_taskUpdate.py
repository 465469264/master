from httprunner import HttpRunner, Config, Step, RunRequest
#新建学服任务
class task_taskUpdate(HttpRunner):
    config = (
        Config("新建/修改学服任务")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("新建/修改通知型学服任务")
                .post("/task/taskUpdate.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Host": "${ENV(Host)}",
                "Cookie":"$Cookie"
            })
            .with_data({
                        "taskId": "",
                        "exType": "$exType",
                        "eyIds": "",
                        "_web_token": "$_web_token",
                        "taskTitle": "$taskTitle",                                      #任务名称
                        "startTimeInput": "$startTimeInput",
                        "startTime": "$startTime",
                        "endTimeInput": "$endTimeInput",
                        "endTime": "$endTime",
                        "taskContent": "测试",                                              #任务描述
                        "eyId": "",
                        "gkEyId": "",
                        "gkUnifiedId": "",
                        "diplomaId": "",
                        "semester": "",
                        "templateId": "",
                        "studentDataCollect": "",
                        "taskUrl": "",
                        "graduationData": "",
                        "taskType": "$taskType",                                        #任务类型   1>任务通知型
                        "zkTemplateId": "",
                        "signatureId": "",
                        "handbookId": "",
                        "commitmentId": "",
                        "isAllow": "$isAllow",                                          #是否启用             禁用>0             启用>1
                        "isNeedCheck": "$isNeedCheck",                                  #是否需毕业核查       不核查>0      置顶1
                        "isSticky": "$isSticky",                                        #是否APP和公众号置顶  不置顶>0     置顶>1
                         "isStudentSee": "$isStudentSee",                                #对学生可见         不可见>0        可见>1
                        "admin-role-save": ""
            })
                .extract()
                .with_jmespath("body","body")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]