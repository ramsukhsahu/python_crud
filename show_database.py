# import mysql.connector
# con=mysql.connector.connect(host='localhost', user='root', passwd='')
from connection import get_connection
con=get_connection()
mycursor = con.cursor()
mycursor.execute('show databases')
for db in mycursor:
    print(db)