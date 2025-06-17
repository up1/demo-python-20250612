import sqlite3

def open_database():
    con = sqlite3.connect("users.db")
    return con

def close_database(con):
    if con:
        con.close()