import pytest
import requests
from util.excel import e_controller
from sql.mapper import Mapper

class Test_Set_Auto():
    def setup_class(self):
        self.yuantu_table=e_controller("D://自动化接口.xlsx","无感建档业务下单")
        print("------------start-------------")

    def set_auto(self,i,table):
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
        #获取接口返回状态 success则业务成功
        status = str(r.json()['success'])
        #获取接口响应码
        code = str(r.json()['code'])
        # 获取sql参数  建档cardNo
        sql_parm = table.get_value(i, 12)
        conn=Mapper()
        rep = conn.select_auto_set_status(sql_parm)
        if status == 'True':
            return rep[0]
        else:
            return code

    def assert_set_auto_status(self, begin, end, table):
        for i in range(begin,end):
            res=str(self.set_auto(i,table))
            rep = str(table.get_value(i, 9))
            print("预期结果为{},实际结果为{}".format(rep, res))
            assert res == rep

    def test_set_auto(self):
        self.assert_set_auto_status(1,4,self.yuantu_table)


    if __name__ == '__main__':
        pytest.main(['-v', 'test.py'])