import requests
from debugtalk import base64_encode
import base64
import json
from debugtalk import get_not_exist_mobile
import os
from httprunner.loader import load_dot_env_file
class register():
    f_list = [r'C:\Users\46546\Desktop\er_loupractice']  # 根路径
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

    def register1(self):
        mobile = get_not_exist_mobile()
        print(mobile)
        headers = {
            "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
            "Content-Type": "base64.b64encode",
            "Host": "${ENV(app_Host)}",
            # "Host": "test.yzwill.cn"
        }
        s = requests.Session()
        # app_url = "http://27-app.yzwill.cn/proxy/us/loginOrRegister/1.0/"
        app_url = "http://test.yzwill.cn/proxy/us/loginOrRegister/1.0/"
        data = base64.b64encode(json.dumps(dict(body={"mobile": mobile,
                                                      "valicode": "888888"},
                                                header={"appType": "4"})).encode("utf-8"))
        r = s.post(url=app_url,data =data ,headers=headers, verify=False)
        dictJson = r.json()
        print(dictJson)
        token = dictJson["body"]["auth_token"]
        mobile =mobile
        print(token)
        self.w_env(token,mobile)

    def w_env(self,token,mobile):
        """
        更新后台的authtoken，减少登录操作
        :param authtoken:
        :return:
        """
        a=self.search_file(self.f_list)
        # file_dir = os.path.abspath('../..')  # 获取上级路径
        # file_dir = os.path.abspath(os.path.join(os.getcwd(), "../.."))  # 获取上上级路径
        # dot_env_path = os.path.join(file_dir, ".env")
        print(a)
        dot_env = load_dot_env_file(a)
        dot_env.update({'register_auth_token':token})
        dot_env.update({'register_mobile':mobile})
        print(dot_env)
        with open(a, "w") as f:
            for k, v in dot_env.items():
                k_v = k + '=' + str(v)
                f.write(k_v)
                f.write('\n')
if __name__ == '__main__':
    register().register1()