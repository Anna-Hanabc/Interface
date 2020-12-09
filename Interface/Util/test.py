#coding=utf-8
import openpyxl
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)

def load_excel():
    # 加载excel
    open_excel = openpyxl.load_workbook(base_path+"/Case/imooc.xlsx")
    return open_excel

def excel_write_data(row,clos,value):
    '''
    向ecxel中写入数据
    '''
    wb = load_excel()
    wr = wb.active()
    wr.cell(row,clos,value)
    wb.save(base_path+"/Case/imooc.xlsx")

excel_write_data(10,1,'hhhan')

