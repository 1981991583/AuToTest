from sql.DbManage import dbmanage
from config.config_handler import YamlHandler
from sql.mapper import Mapper

conn=Mapper()
#re1=conn.select_card_no()

id= '11f97803f4d141e985a999415785929f'
re=conn.select_user(id)
#print(re[0])

card_no='350000200002043673'
re2=conn.select_auto_set_status(card_no)
print(re2[0])