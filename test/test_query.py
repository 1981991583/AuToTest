import pytest
import requests
from util.excel import e_controller
from sql.mapper import Mapper
import json

class Test_all():

    def setup_class(self):
        self.yuantu_table=e_controller("D://自动化接口.xlsx","档案号查询")
        print("------------start-------------")

    def getResult(self,i,table):
        #获取接口地址
        url=table.get_value(i,3)
        #url = "http://frontgatewayv4-cquat.yuantutech.com/frontgateway/api/patient-info/query-by-account"
        apiName=table.get_value(i,0)
        print("正在执行%s"%apiName)
        #获取响应头
        headers=eval(table.get_value(i,7))
        #请求参数
        body = table.get_value(i,6)
        r = requests.post(url,data=body.encode('utf-8'), headers=headers)
        #数据库参数
        sql_parm=table.get_value(i,12)
        conn=Mapper()
        #数据库查询
        sql_res=conn.select_user(sql_parm)
        rep_res=r.json()['data']['patientName']
        #将接口返回值与数据库中的值进行比较
        if rep_res == sql_res[0]:
            return rep_res
        else:
            return 0


    def assert_status(self,begin,end,table):
        for i in range(begin,end):
            name=self.getResult(i,table)
            #预期结果
            res = table.get_value(i,9)
            print("result = %s,预期结果为:%s"%(name,res) )
            pytest.assume (name == table.get_value(i,9))

    def test_query(self):
        self.assert_status(1,self.yuantu_table.get_nrows(),self.yuantu_table)

    if __name__ == '__main__':
        pytest.main(['-s', 'test_query.py'])




