import json
import os
import yaml
from httprunner.compat import ensure_path_sep

try:
    from utils.yapi import read_yapi

    # 接口名称列表
    spc_dict = read_yapi()
except:
    spc_dict = None


def har_to_yml_or_json(path="har", file_type='yml'):
    """
    har文件转为yml或者json
    :param file_type:要转换的文件类型，默认为yml
    :param path: 文件相对项目位置的目录
    :return: r 返回运行信息
    """
    file_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # 获取上级路径
    har_dir = file_dir + "\\" + path  # 文件目录
    har_list = []  # har文件列表
    listdir(har_dir, har_list)  # 获取所有.har文件
    cmd = ""
    if file_type is "yml":
        t = " -2y & "
    elif file_type is "json":
        t = ' & '
    else:
        print("要转换的文件类型不支持")  # 打印返回内容
        return False
    # 遍历.har文件列表，把拼接生成yml文件cmd命令
    for har in har_list:
        cmd += "har2case " + har + t
    print(cmd)
    d = os.popen(cmd)  # 执行cmd
    r = d.read()  # 获取cmd的返回内容
    print(r.encode("GBK"))  # 打印返回内容
    return r


def listdir(path, file_list, file_end=".har"):  # 传入存储的list
    """
    将目录下file_end结尾的文件存入list中
    :param path:文件目录
    :param file_list:存储的文件的list
    :param file_end:查找文件的结尾，可以是字符串，也可以是列表
    """
    if os.path.isdir(path):
        for file in os.listdir(path):  # 逐层遍历目录，并把file_end结尾文件添加到列表
            # 过滤不要的文件与目录
            if file == ".pytest_cache" or file == "__init__.py" or file == "__pycache__":
                continue
            file_path = os.path.join(path, file)
            file_path = ensure_path_sep(file_path)  # 报告路径
            if os.path.isdir(file_path):
                listdir(file_path, file_list, file_end)
            else:
                suffix = os.path.splitext(file_path)[-1]
                # 判断文件结尾是列表时，判断后缀名是否在其中，当是字符串时，后缀名是否相等
                if (type(file_end) == list and suffix in file_end) or suffix == file_end:
                    file_list.append(file_path)
    else:
        file_list.append(path)


def jsonlist_to_yml(file_path="har"):
    """
    json列表文件转换为yml
    :param file_path: 文件相对项目位置的目录
    :return:
    """
    file_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # 获取上级目录
    file_name = file_dir + "\\" + file_path  # 文件目录
    json_list = []  # json文件列表
    listdir(file_name, json_list, ".json")  # 获取所有.json文件
    # 遍历所有json文件
    for filename in json_list:
        json_to_yml(filename)  # 保存json到


def json_to_yml(filename, path='har\\yml'):
    """
    json文件里多个api转换为单个api的yml文件，并保存在  项目目录/har/yml 下,一个json转化为一个测试用例
    :param filename:json文件路径
    :param path:
    """
    file_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "\\" + path  # 获取上级目录 +'\\har\\yml\\'
    try:
        os.makedirs(file_dir + "\\" + 'testcases')  # 创建api和测试用例的多层目录
    except FileExistsError:
        pass
    # 读取json文件
    with open(filename, "r", encoding='utf8') as f:
        gpd_list = json.loads(f.read())  # json转为字典
    gpd_list["config"]["base_url"] = "${ENV(Host)}"  # 把base_url配置为虚拟环境中
    testcase_dict = {'config': gpd_list.get('config'), 'teststeps': []}  # 测试用例的的dict
    # 遍历list，将json格式的api转为yml格式并保存到文件中
    for teststep in gpd_list.get("teststeps"):
        teststep["request"]["url"] = teststep.get("name")  # 把url去掉域名
        step_list = teststep.get('name').split('/')  # 把url分割为列表
        # 最后一位为数字时，找倒数第二，直到不是数字，如果有?，则取?前面的为文件名，反之直接为文件名
        while 1:
            try:
                float(step_list[-1])
                step_list.pop()
            except:
                if "?" in step_list[-1]:
                    step_list[-1] = step_list[-1].split('?')[0]
                elif step_list[-1] == "selectList" or step_list[-1] == "list" or step_list[-1] == "queryByPage":
                    step_list[-1] = step_list[-2] + "List"
                elif step_list[-1] == "updateOne":
                    step_list[-1] = "update" + step_list[-2].capitalize()
                elif step_list[-1] == "deleteOne":
                    step_list[-1] = "delete" + step_list[-2].capitalize()
                elif step_list[-1] == "saveOne" or step_list[-1] == "doSave":
                    step_list[-1] = "save" + step_list[-2].capitalize()
                elif step_list[-1] == "selectOne":
                    step_list[-1] = "select" + step_list[-2].capitalize() + "One"
                elif step_list[-1] == "toEdit":
                    step_list[-1] = "edit" + step_list[-2].capitalize()
                elif step_list[-1] == "toView":
                    step_list[-1] = step_list[-2] + "Details"
                elif step_list[-1] == "saveOrUpdate" or step_list[-1] == "insert":
                    step_list[-1] = "saveOrUpdate" + step_list[-2].capitalize()
                elif step_list[-1] == "deleteById":
                    step_list[-1] = "delete" + step_list[-2].capitalize()
                elif step_list[-1] == "doQuery":
                    step_list[-1] = step_list[-2] + "DoQuery"
                elif step_list[-1] == "updateStatus":
                    step_list[-1] = step_list[-2] + "UpdateStatus"
                elif step_list[-1] == "":
                    step_list[-1] = step_list[-2]
                break
        api_file = step_list[-1] + '_' + teststep["request"]["method"]  # 文件名为例如：login_POST
        if spc_dict:
            teststep["name"] = spc_dict.get(api_file, '无')  # 获取接口名称
        api_dict = {'config': gpd_list.get('config'), 'teststeps': [teststep]}  # 单个api的dict
        testcase_dict['teststeps'].append(
            {'name': teststep["name"], 'api': (path + '\\' + api_file + '.yml')})  # 拼接测试用例
        api_file = file_dir + "\\" + api_file + '.yml'  # 文件路径
        save_yml(api_dict, api_file)  # 保存为yml文件

    testcase_file = filename.split('\\')[-1]  # 取路径分割后的最后一位xxx.json
    testcase_file = testcase_file.split('.')[0]  # 取出文件名称
    testcase_file = file_dir + "\\" + 'testcases' + '\\' + testcase_file + '.yml'  # 文件路径
    save_yml(testcase_dict, testcase_file)  # 保存测试用例


def save_yml(test_dict, filey):
    """
    保存为yml文件
    :param test_dict: 要保存的字典
    :param filey: 保存的文件路径
    """
    dstr = json.dumps(test_dict)  # dict转成字符
    dyaml = yaml.load(dstr)  # 将字符转仓yaml
    stream = open(filey, 'w', encoding='utf8')  # yml写入
    yaml.safe_dump(dyaml, stream, default_flow_style=False, allow_unicode=True)  # 输出到文件中


if __name__ == '__main__':
    # 批量har文件转换为json或yml
    har_to_yml_or_json(path="har\\new", file_type='json')
    # 批量把jsonlist转化为yml
    jsonlist_to_yml("har\\new")
