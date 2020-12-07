#coding=utf-8
import openpyxl
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from Util.handle_excel import excel_data
from Base.base_request import request

class RunMain:
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            #i是从0开始的，excel中第一行内容的行号是i=2
            data = excel_data.get_rows_value(i+2)
            # print(data)
            #['imooc_001', '登录', 'yes', 'create_user', '/login/', 'post', '{"username":"111111"}', 'yes', 'message', None]
            is_run = data[2]
            if is_run == "yes":
                url = data[5]
                method = data[6]
                data1 = data[7]
                res = request.run_main(method,url,data1)
                print(res)

if __name__ == "__main__":
    run = RunMain()
    run.run_case()