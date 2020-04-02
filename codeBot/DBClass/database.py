import pymysql
import cryptography
import config

class Database:

    hostname = config.hostname
    username = config.username
    password = config.password
    db_name =  config.db_name
    table_name = config.table_name

    con = None
    cursor = None
    is_connected = None

    def __init__(self):
        try:
            self.con = pymysql.connect(self.hostname, 
                                    self.username,
                                    self.password,
                                    self.db_name)

            self.cursor = self.con.cursor()
            self.is_connected = True
        except pymysql.OperationalError:
            self.is_connected = False
           

    def insert_data(self, adv_info):
        if self.is_connected:
            self.cursor.execute("""INSERT INTO {TABLE} 
                                (username, type_of_adv, product_type, dop_info, phone_number) 
                                VALUES (%s,%s,%s,%s,%s)""".format(
                TABLE = self.table_name, 
                ), adv_info)
            self.con.commit()
            return 'ok'
        else:
            return 'error'






