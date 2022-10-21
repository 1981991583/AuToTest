import pytest
import requests
from util.excel import e_controller
from sql.mapper import Mapper

class Test_query_byCard():
    def setup_class(self):
        self.yuantu_table=e_controller("D://自动化接口.xlsx","用户卡查询 ")
        print("------------start-------------")

    def query_byCard(self,i,table):
        url = table.get_value(i, 3)
        # url = "http://frontgatewayv4-cquat.yuantutech.com/frontgateway/api/patient-info/query-by-account"
        apiName = table.get_value(i, 0)
        print("正在执行%s" % apiName)
        headers = eval(table.get_value(i, 7))
        # headers = {'Content-Type': "application/json"}
        # 获取请求参数
        body = table.get_value(i, 6)
        # 预期结果
        res_phone = table.get_value(i, 9)
        # 获取sql参数
        sql_parm = table.get_value(i, 12)
        conn=Mapper()
        #数据库中根据卡号查询的姓名
        rep=conn.select_name_by_cardNo(sql_parm)
        r = requests.post(url, data=body.encode('utf-8'), headers=headers)
        # print(r.json())
        status = str(r.json()['success'])
        code = str(r.json()['code'])
        print(status)

        if status == 'True':
            return rep[0]
        else:
            return code

    # def assert_query_byCardNo(self,begin,end,table):
    #     for i in range(begin,end):

    def test(self):
       print(self.query_byCard(1,self.yuantu_table))
