import pytest
import requests
from util.excel import e_controller
from sql.mapper import Mapper

class Test_modify():

    yuantu_table = e_controller("D://自动化接口.xlsx", "修改档案信息")



    def modify1(self,i,table):
        # 获取行数
        # end=self.yuantu_table.get_nrows()
        url = table.get_value(i, 3)
        # url = "http://frontgatewayv4-cquat.yuantutech.com/frontgateway/api/patient-info/query-by-account"
        apiName = table.get_value(i, 0)
        print("正在执行%s" % apiName)
        headers = eval(table.get_value(i, 7))
        # headers = {'Content-Type': "application/json"}
        #获取请求参数
        body = table.get_value(i, 6)
        #预期结果
        res_phone = table.get_value(i, 9)
        #获取sql参数
        sql_parm = table.get_value(i,12)
        r = requests.post(url, data=body.encode('utf-8'), headers=headers)
        res=r.json()
        print(r.json())
        return res

    # def test_null(self):
    #     a1=self.modify1(9,self.yuantu_table)[1]
    #     print(a1)
    #     a2=str(a1)
    #     if a2 =='False':
    #         print(1)
    #     else :
    #         print(2)
    def test_modify(self):
        print(self.modify1(1,self.yuantu_table))