from DBfunction import *
from Mapper import Mapper


conn = sql_connection()
rows = sql_select(conn)

for contract in rows:
    Mapper(*contract, term=2).create()
    print("----------------------------------------------------------------------------------------------------------")




