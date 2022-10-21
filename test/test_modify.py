import ast
import time

import pytest
import requests
from util.excel import e_controller
from sql.mapper import Mapper

class Test_modify():

    def setup_class(self):
        self.yuantu_table=e_controller("D://自动化接口.xlsx","修改档案信息")
        print("------------start-------------")

    def modify(self,i,table):
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
        res= table.get_value(i, 9)
        #获取sql参数
        sql_parm = table.get_value(i,12)
        r = requests.post(url, data=body.encode('utf-8'), headers=headers)
        #print(r.json())
        status=str(r.json()['success'])
        #phone=r.json()['data']['phone']
        code=str(r.json()['code'])
        conn=Mapper()
        #数据库中对应的值
        rep=conn.select_phone(sql_parm)
        #print(r.json())
        #如果状态为success，则返回存入到数据库中的值，否则返回响应码
        if status == 'True':
            return rep[0]
        else:
            return code

    # def assert_data(self,i,table):
    #     url = table.get_value(i, 3)
    #     headers = eval(table.get_value(i, 7))
    #     # headers = {'Content-Type': "application/json"}
    #     # 获取请求参数
    #     body = table.get_value(i, 6)
    #     r = requests.post(url, data=body.encode("utf-8"), headers=headers)
    #     return (r.json()['data'])
    #
    # def assert_success(self,i,table):
    #     url = table.get_value(i, 3)
    #     headers = eval(table.get_value(i, 7))
    #     # headers = {'Content-Type': "application/json"}
    #     # 获取请求参数
    #     body = table.get_value(i, 6)
    #     r = requests.post(url, data=body.encode("utf-8"), headers=headers)
    #     return (r.json()['success'])

    def assert_result(self,begin,end,table):
        for i in range(begin,end):
            res=self.modify(i,table)
            #判断data是否为空
            # data=self.assert_data(i,table)
            # if_success=str(self.assert_success(i,table))
            #预期结果
            rep=table.get_value(i,9)
            print("预期结果为{},实际结果为{}".format(rep,res))
            assert res == rep


    def test_modify(self):
        self.assert_result(1,self.yuantu_table.get_nrows(),self.yuantu_table)


    if __name__ == '__main__':
        pytest.main(['-s', 'test_modify.py'])

    '''def test_registration(self):
        print(self.modify(1,self.yuantu_table))'''