import pymysql
from config.config_handler import YamlHandler

class dbmanage():
    def __init__(self):
        YAML = YamlHandler('D:\pythonProject1\config\config.yaml')
        yaml_data = YAML.read_yaml()
        host = yaml_data['mysql']['host']
        user = yaml_data['mysql']['user']
        password = yaml_data['mysql']['password']
        database = yaml_data['mysql']['database']
        charset = yaml_data['mysql']['charset']
        self.conn = pymysql.connect(host=host, user=user, password=password, database=database, charset=charset)
        # 得到一个可以执行sql语句的光标对象,dictCursor:以字典形式输出
        self.DictCursor = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def select_execute(self, sqlcode):
        self.DictCursor.execute(sqlcode)
        ret = list(self.DictCursor.fetchall())
        #print(sqlcode + "————已执行")
        return ret

    def other_execute(self, sqlcode, sqlname):
        try:
            self.cursor.execute(sqlcode)
            print("执行sql语句——————{}".format(sqlcode))
            self.conn.commit()
            print(sqlname + "————执行成功")
        except:
            print(sqlcode)
            self.conn.rollback()
            print(sqlname + "————执行失败")