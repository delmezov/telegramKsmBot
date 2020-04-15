import sqlite3

con = sqlite3.connect("mydatabase.db")

cursor = con.cursor()

cursor.execute("""CREATE TABLE advDB
                  (username, type_of_adv, product_type,
                   dop_info, phone_number)
               """)
con.commit

