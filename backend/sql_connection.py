import datetime
import mysql.connector

__cnx = None


def get_sql_connection():
    print("Opening mysql connection")
    global __cnx

    if __cnx is None:
        __cnx = mysql.connector.connect(
            host='database-1.ck91hoycczjt.us-east-1.rds.amazonaws.com', port=3306, user='admin', password='Kura123.com', database='grocery_store')

    return __cnx
