import pytest
import requests
from util.excel import e_controller
from sql.mapper import Mapper

class Test_back_registration():
    def setup_class(self):
        self.yuantu_table=e_controller("D://自动化接口.xlsx","无感建档业务下单")
        print("------------start-------------")

    def back_registration(self,i,table):
        # 获取行数
        # end=self.yuantu_table.get_nrows()
        url = table.get_value(i, 3)
        # url = "http://frontgatewayv4-cquat.yuantutech.com/frontgateway/api/patient-info/query-by-account"
        apiName = table.get_value(i, 0)
        print("正在执行%s" % apiName)
        headers = eval(table.get_value(i, 7))
        # headers = {'Content-Type': "application/json"}
        body = table.get_value(i, 6)
        res_No = table.get_value(i, 9)
        r = requests.post(url, data=body.encode('utf-8'), headers=headers)