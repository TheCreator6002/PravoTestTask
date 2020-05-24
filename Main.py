from DBfunction import *
from Mapper import Mapper


conn = sql_connection()
rows = sql_select(conn)

for row in rows:
    contract = Mapper(*row).create()
    contract.payment_calculation(term=2)
    print("----------------------------------------------------------------------------------------------------------")




