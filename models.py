"""
This is used to hold database functions
"""

import sqlite3 as sql
def create_database():
    sqlite_file = 'database.db'  # name of the sqlite database file
    table_name = 'users'  # name of the table to be created
    id_column = 'id_column'

    # Connecting to the database file
    conn = sql.connect(sqlite_file)
    c = conn.cursor()

    # Creating a new SQLite table
    c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY key , username text not null, password text not NULL)')


def insertUser(username, password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username, password))
    con.commit()
    con.close()




# This method takes a string and returns whether or not a user with the username enter exists


# gets users searches, returns list of searches


def getPassword(uname):
    uname = uname
    con = sql.connect("database.db")
    c = con.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (uname,))
    # format(tn='users'))
    data = c.fetchall()
    d = data[0]
    # print(data[0])
    return d[0]
    con.close()


# returns the ID of a given username
def getId(uname):
    uname = uname
    con = sql.connect("database.db")
    c = con.cursor()
    c.execute("SELECT id_column FROM users WHERE username = ?", (uname,))
    data = c.fetchall()
    d = data[0]
    # print(data[0])
    return d[0]
    con.close()


