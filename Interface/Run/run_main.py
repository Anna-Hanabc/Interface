#coding=utf-8
import openpyxl
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from Util.handle_excel import excel_data
from Base.base_request import request
from Util.handle_result import handle_result,handle_result_json,get_result_json
import json

class RunMain:
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            # i是从0开始的，excel中第一行内容的行号是i=2
            data = excel_data.get_rows_value(i+2)
            #['imooc_001', '登录', 'yes', 'create_user', '/login/', 'post', '{"username":"111111"}', 'yes', 'message', None]
            is_run = data[2]
            except_method = data[10]
            except_result = data[11]
            if is_run == "yes":
                url = data[5]
                method = data[6]
                data1 = data[7]
                res = request.run_main(method,url,data1)
                #int和str无法比较，需要强转一下
                code = str(res['errorCode'])
                desc = res['errorDesc']
                #如果预期结果方式为mec：message+errorcode
                if except_method == "mec":
                    config_message = handle_result(url,code)
                    if desc == config_message:
                        excel_data.excel_write_data(i+2,12,"通过")
                        print("case通过")
                    else:
                        excel_data.excel_write_data(i+2,12,"失败")
                        excel_data.excel_write_data(i+2,13,json.dumps(res))
                        print("case失败")
                if except_method == "errorcode":
                    if except_result == code:
                        excel_data.excel_write_data(i+2,12,"通过")
                        print("case通过")
                    else:
                        excel_data.excel_write_data(i+2,12,"失败")
                        excel_data.excel_write_data(i+2,13,json.dumps(res))
                        print("case失败")
                # 如果预期结果方式为json格式
                if except_method == "json":
                    if code == 1000:
                        status_str="sucess"
                    else:
                        status_str="error"
                    except_result_json = get_result_json(url,status_str)
                    # print(res,'-------',except_result_json)
                    result = handle_result_json(res,except_result_json)
                    if result:
                        excel_data.excel_write_data(i+2,12,"通过")
                        print("case通过")
                    else:
                        excel_data.excel_write_data(i+2,12,"失败")
                        excel_data.excel_write_data(i+2,13,json.dumps(res))
                        print("case失败")


if __name__ == "__main__":
    run = RunMain()
    run.run_case()