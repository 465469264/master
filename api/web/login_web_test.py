import requests
from httprunner.loader import load_dot_env_file
import base64
import json
from debugtalk import base64_encode
import os
file_dir = os.path.abspath('../..')  # 获取上级路径
dot_env_path = os.path.join(file_dir, ".env")
class login():
    f_list = [r'C:\Users\Administrator\Desktop\er_loupractice']  # 根路径
    f_str = '.env'
    def search_file(self,f_list):
        s_list = f_list.copy()
        f_list.clear()
        for x_dir in s_list:
            if os.path.isdir(x_dir):
                try:
                    for fname in os.listdir(x_dir):
                        fpath = os.path.join(x_dir, fname)
                        if self.f_str in fname and os.path.isfile(fpath):
                            print(fpath)
                            return fpath
                        elif os.path.isdir(fpath):
                            # 保存下一级目录
                            f_list.append(fpath)
                except IOError:
                    print("错的", x_dir)

    def login(self):
        s = requests.Session()
        data = {"isOpenImage": "",
                "mobile": "18221823862",
                "ImgValidCode": "",
                "validCode": "888888"}
        url = "http://bms.yzwill.cn/loginByMobile.do"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "uri": "http://bms.yzwill.cn/toLogin.do",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        res = s.post(url=url, headers=headers, data=data)
        print(res)
        cookie = requests.utils.dict_from_cookiejar(res.cookies)["SESSION"]
        webcookie = "SESSION=" + cookie
        self.w_env(webcookie)

    def w_env(self,webcookie):
        """
        更新后台的authtoken，减少登录操作
        :param authtoken:
        :return:
        """
        a=self.search_file(self.f_list)
        print(a)
        dot_env = load_dot_env_file(a)
        dot_env.update({'COOKIE':webcookie})
        print(dot_env)
        with open(a, "w") as f:
            for k, v in dot_env.items():
                k_v = k + '=' + str(v)
                f.write(k_v)
                f.write('\n')

if __name__ == '__main__':
    login().login()
