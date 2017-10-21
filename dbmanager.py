"""
This is a utility to check and modify the database for testing purposes, has no use for end users, just for developers
"""

import sqlite3
import models


def create_database():
    sqlite_file = 'database.db'  # name of the sqlite database file
    table_name = 'users'  # name of the table to be created
    id_column = 'id_column'

    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    # Creating a new SQLite table
    c.execute('CREATE TABLE users({nf} {ft})' \
              .format( nf=id_column, ft='INTEGER PRIMARY KEY AUTOINCREMENT'))

    # add next column
    new_column = 'username'
    column_type = 'TEXT'
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}" \
              .format(tn=table_name, cn=new_column, ct=column_type))

    # add next column
    new_column = 'password'
    column_type = 'TEXT'
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}" \
              .format(tn=table_name, cn=new_column, ct=column_type))


    print("Database and table created")
    # Committing changes and closing the connection to the database file
    conn.commit()
    conn.close()


# prints all user data in users table
