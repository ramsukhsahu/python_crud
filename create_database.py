import mysql.connector
con=mysql.connector.connect(host='localhost', user='root', passwd='')
mycursor = con.cursor()
mycursor.execute('create database python_db')