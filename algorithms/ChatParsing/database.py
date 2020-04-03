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

    def create_table(self):
        if self.is_connected:
            self.cursor.execute("""CREATE TABLE {TABLE}
                  (
                  id INT AUTO_INCREMENT PRIMARY KEY,
                  username VARCHAR(255), 
                  type_of_adv VARCHAR(255), 
                  product_type VARCHAR(255),
                  phone_number VARCHAR(255),
                  data VARCHAR(255))
               """.format(
                   TABLE = self.table_name
               ))

            self.con.commit()
           

    def insert_data(self, adv_info):
        if self.is_connected:
            self.cursor.execute("""INSERT INTO {TABLE} 
                                (username, type_of_adv, product_type, phone_number, data) 
                                VALUES (%s,%s,%s,%s,%s)""".format(
                TABLE = self.table_name
                ), adv_info)
            self.con.commit()
            return 'ok'
        else:
            return 'error'



#Database().create_table()



