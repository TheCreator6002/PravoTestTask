import sqlite3
from sqlite3 import Error


def sql_connection():
    # Create database
    try:
        conn = sqlite3.connect("test_database.db")
        print("Connection is established: Database is created")
        return conn
    except Error:
        print(Error)


def sql_table(conn):
    # Create table
    cursorObj = conn.cursor()

    cursorObj.execute("""CREATE TABLE "contracts" (
                         `Id` INTEGER PRIMARY KEY,
                         `PeriodMonths` INTEGER NOT NULL,
                         `Amount` MONEY NOT NULL,
                         `Date` DATE NOT NULL);""")
    conn.commit()


def sql_insert(conn, insertDate):
    # Insert into database
    cursorObj = conn.cursor()

    for date in insertDate:
        cursorObj.execute("INSERT INTO `contracts`(`PeriodMonths`, `Amount`, `Date`) VALUES (?,?,?)", date)

    conn.commit()


def sql_select(conn):
    # get selected column
    cursorObj = conn.cursor()

    cursorObj.execute("SELECT `Id`, `PeriodMonths`, `Amount`, `Date` FROM `contracts`")

    rows = cursorObj.fetchall()

    return rows



