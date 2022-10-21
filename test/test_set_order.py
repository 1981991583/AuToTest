import pytest
import requests
from util.excel import e_controller

class Test_set_order():

    def setup_class(self):
        self.yuantu_table=e_controller("D://自动化接口.xlsx","建档业务下单")


    def getResult(self,i,table):

        url = table.get_value(i, 3)
        # url = "http://frontgatewayv4-cquat.yuantutech.com/frontgateway/api/patient-info/query-by-account"
        apiName = table.get_value(i, 0)
        print("正在执行%s" % apiName)
        headers = eval(table.get_value(i, 7))
        # headers = {'Content-Type': "application/json"}
        body = table.get_value(i, 6)
        r = requests.post(url, data=body.encode("utf-8"), headers=headers)
        code=str(r.json()['success'])
        return code

    def assert_result(self,begin,end,table):
        for i in range(begin,end):
            res=self.getResult(i,table)
            rep=str(self.yuantu_table.get_value(i,9))
            print("建档下单响应码为:%s,预期结果为%s" % (res, rep))
            assert res == rep

    def test1(self):
        print(self.assert_result(1,self.yuantu_table.get_nrows(),self.yuantu_table))