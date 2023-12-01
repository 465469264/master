import pytest
import allure
import os
import urllib3
urllib3.disable_warnings()
import shutil
# C:\Users\46546\Desktop\er_loupractice\testcases\test_Main_Process\Junior_College
if __name__ == '__main__':
    f_list = os.path.dirname(os.path.abspath(__file__))
    print(f_list)
    # 生成allure-report
    # 读取文件路径设置
    report_name = os.path.join(f_list + "/testcases/test_Main_Process/Junior_College")
    report_temp = os.path.join(f_list + "/logs/temp")
    print(report_name)
    print(report_temp)

    # 生成allure-result
    pytest.main([report_name, "-s", "--alluredir", report_temp])
    # 生成allure-report
    os.system(f"allure generate {report_temp} -o ../logs/report --clean ")
    os.system('allure serve ./losg/temp')

    # 判断缓存目录是否存在，如果存在就删除
    if os.path.exists(os.path.join(f_list + "/.pytest_cache")):
        shutil.rmtree(os.path.join(f_list + "/.pytest_cache"))
        print("已删除旧的缓存目录")

    #删除logs下得temp
    if os.path.exists(report_temp):
        shutil.rmtree(report_temp)
        print("已删除temp")

