import xlrd2

class e_controller():
    # 修改为通过表名称获取
    def __init__(self, excelname, name):
        self.data = xlrd2.open_workbook(excelname)
        self.table = self.data.sheet_by_name(name)
        print('*************table',self.table)
        self.workbook = xlrd2.open_workbook(excelname)
        self.worksheet = self.workbook.sheet_by_name(name)

    # 读取excel
    def get_value(self, rowx, colx):
        return self.table.cell_value(rowx, colx)

    # 获取有效行数
    def get_nrows(self):
        return self.table.nrows

    # 获取有效列数
    def get_ncols(self):
        return self.table.ncols

    # 写入excle,0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error, 6 blank
    def set_value(self, row, col, value):
        self.worksheet.write(row, col, value)
        self.workbook.save("D:\\result.xls")

