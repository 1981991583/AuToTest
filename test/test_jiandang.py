from imp import reload

import pytest
import requests
from util.excel import e_controller
from sql.mapper import Mapper

class Test_jiandang():

    def setup_class(self):
        self.yuantu_table=e_controller("D://自动化接口.xlsx","建档")
        print("------------start-------------")

    def jiandang(self,i,table):

        #获取行数
        #end=self.yuantu_table.get_nrows()
        url = table.get_value(i, 3)
        # url = "http://frontgatewayv4-cquat.yuantutech.com/frontgateway/api/patient-info/query-by-account"
        apiName = table.get_value(i, 0)
        print("正在执行%s" % apiName)
        headers = eval(table.get_value(i, 7))
        # headers = {'Content-Type': "application/json"}
        body = table.get_value(i, 6)
        res_No=table.get_value(i,9)
        r = requests.post(url, data=body.encode("utf-8"), headers=headers)
        print(r.json())
        return res_No

    def assert_cardNo(self,begin,end,table):
        for i in range(begin,end):
            card_no=self.jiandang(i,table)
            print('预期结果:%s'%card_no)
            sql_pool = Mapper()
            #在数据库中查询卡号
            card_pool = sql_pool.select_card_no()
            assert card_no in card_pool

    def test_set(self):
        self.assert_cardNo(1,2,self.yuantu_table)

    if __name__=="__main__":
        pytest.main(["-v","test.py"])
