import pytest
import os
import urllib3
urllib3.disable_warnings()
import shutil
if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(__file__))
    # 生成allure-report
    # 读取文件路径设置
    report_name = os.path.join(base_dir + "/er_loupractice", "testcases")
    report_temp = os.path.join(base_dir + "/er_loupractice", "log/temp")

    # 生成allure-result
    pytest.main([report_name, "-s", "--alluredir", report_temp])
    # 生成allure-report
    os.system(f"allure generate {report_temp} -o ../logs/report --clean ")
    os.system('allure serve ./log/temp')

    #判断archive是否存在，如果存在就删除
    if os.path.exists(r"C:\Users\46546\Desktop\er_loupractice\.pytest_cache"):
        shutil.rmtree(r"C:\Users\46546\Desktop\er_loupractice\.pytest_cache")
        print("已删除archive文件")

    # 删除log下得temp
    if os.path.exists(r"C:\Users\46546\Desktop\er_loupractice\logs\temp"):
        shutil.rmtree(r"C:\Users\46546\Desktop\er_loupractice\logs\temp")
        print("已删除archive文件")
    # 判断缓存目录是否存在，如果存在就删除
    if os.path.exists(r"C:\Users\46546\Desktop\er_loupractice\.pytest_cache"):
        shutil.rmtree(r"C:\Users\46546\Desktop\er_loupractice\.pytest_cache")
        print("已删除旧的缓存目录")

