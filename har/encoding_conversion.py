# coding:utf-8
import os
import chardet

from har.file_conversion import listdir


# 单个文件的编码转换
def file_encoding_conversion(file_path, new_encoding="UTF-8"):
    """
    单个文件的编码转换
    :param file_path: 文件路径
    :param new_encoding: 新的编码
    :return:
    """
    file_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # 获取上级路径
    # 判断是否是绝对路径，如果不是
    if not os.path.isabs(file_path):
        # 加上路径
        file_path = os.path.join(file_dir, file_path)
    # 判断是否是文件路径
    if os.path.isfile(file_path):
        # 二进制读取
        with open(file_path, 'rb') as f:
            data = f.read()
            tmp = chardet.detect(data)
            old_encoding = tmp.get("encoding")
        if old_encoding.lower() == "gb2312":
            old_encoding = "gbk"
        if old_encoding.lower() != new_encoding.lower():
            # 读取文件
            with open(file_path, 'r', encoding=old_encoding) as f:
                data = f.read()
                # 将文件转换成GBK编码
                with open(file_path, 'w', encoding=new_encoding) as fp:  # 指定编码读
                    fp.write(data)
                    fp.close()
    else:
        print("这不是一个文件路径")

a = file_encoding_conversion(r'C:\Users\46546\Desktop\er_loupractice\.env')
# 批量转换文件编码
# def batch_file_encoding_conversion(file_path, file_end=None, new_encoding="utf-8"):
#     """
#     批量转换文件编码
#     :param file_path:文件目录，可以是文件，也可以是目录
#     :param file_end:后缀名，可以是一个list，也可以是字符串
#     :param new_encoding:新的编码
#     :return:
#     """
#     file_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # 获取上级路径
#     if not os.path.isabs(file_path):
#         # 加上路径
#         file_path = os.path.join(file_dir, file_path)  # 确定源文件字符编码
#     file_list = []  # 文件列表
#     if not file_end:
#         file_end = ".env"     # 默认是csv文件后缀名
#     listdir(file_path, file_list, file_end)  # 获取所有".csv"文件
#     for fp in file_list:    # 遍历csv文件，并进行修改
#         file_encoding_conversion(fp, new_encoding=new_encoding)


# if __name__ == '__main__':
#     # file_path = 'E:\\python\\project\\httpRunerSPC\\data'
#     file_path = 'data'
#     batch_file_encoding_conversion(file_path)
