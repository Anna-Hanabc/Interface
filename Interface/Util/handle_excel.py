#coding=utf-8
import openpyxl
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)

# open_excel = openpyxl.load_workbook(base_path+"/Case/imooc.xlsx")
# sheet_name = open_excel.sheetnames
# excel_value = open_excel[sheet_name[0]]
# print(excel_value)

# print(excel_value.cell(1,3).value)
# print(excel_value.max_row)
# print(excel_value.max_column)


class HandleExcel():
    def load_excel(self):
        # 加载excel
        open_excel = openpyxl.load_workbook(base_path+"/Case/imooc.xlsx")
        return open_excel
    def get_sheet_data(self,index=None):
        # 加载所有sheet
        sheet_name = self.load_excel().sheetnames
        if index == None:
            index = 0
        data = self.load_excel()[sheet_name[index]]
        return data
    def get_cell_value(self,row,col):
        # 获取某一个单元格内容
        data = self.get_sheet_data().cell(row=row,column=col).value
        return data
    def get_rows(self):
        # 获取最大行数
        row = self.get_sheet_data().max_row
        return row
    def get_rows_value(self,row):
        # 获取某一行的内容
        row_list = []
        for i in self.get_sheet_data()[row]:
            row_list.append(i.value)
        return row_list

    def excel_write_data(self,row,clos,value):
        '''
        向ecxel中写入数据
        '''
        wb = self.load_excel()
        wr = wb.active()
        wr.cell(row,clos,value)
        wb.save(base_path+"/Case/imooc.xlsx")


excel_data = HandleExcel()

if __name__ == "__main__":
    handle = HandleExcel()
    # print(handle.get_cell_value(2,5))
    # print(handle.get_rows())
    # print(handle.get_rows_value(2))
    # handle.excel_write_data(10,1,'hhhan') 这里没有调通
    pass