import xlrd2
from util.excel import e_controller

table=e_controller("D://自动化接口.xlsx","修改档案信息")

print(table.get_value(1,3))

for i in range(1,3):
    print(i)