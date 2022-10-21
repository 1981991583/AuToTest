from sql.DbManage import dbmanage
import time
from config.config_handler import YamlHandler
from datetime import datetime, date, timedelta

    
class Mapper():
    def __init__(self):
        self.db = dbmanage()
        self.yaml = YamlHandler('D:\pythonProject1\config\config.yaml')
        self.yaml_data = self.yaml.read_yaml()

    def select_user(self,userAccountId):
        res = self.db.select_execute("select patient_name from ad_user_account where id = '{}'".format(userAccountId))
        res2 = [item[key] for item in res for key in item]
        return res2

    def select_card_no(self):
        res = self.db.select_execute("select card_no from ad_user_account ")
        res2 = [item[key] for item in res for key in item]
        return res2

    def select_phone(self,userAccountId):
        res = self.db.select_execute("select phone from ad_user_account where id ='{}'".format(userAccountId))
        res2 = [item[key] for item in res for key in item]
        return res2

    def select_order_status(self,card_no):
        res = self.db.select_execute("select status from ad_set_patient_business_order where card_no = '{}'".format(card_no))
        res2 = [item[key] for item in res for key in item]
        return res2

    def select_name_by_cardNo(self,card_no):
        res = self.db.select_execute("select patient_name from ad_user_account where card_no = '{}'".format(card_no))
        res2 = [item[key] for item in res for key in item]
        return res2

    def select_auto_set_status(self,card_no):#无感建档 查询数据库中建档状态
        res = self.db.select_execute("select status from ad_set_patient_business_order where card_no = '{}'".format(card_no))
        res2 = [item[key] for item in res for key in item]
        return res2
