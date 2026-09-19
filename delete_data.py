from connection import get_connection
con=get_connection()
mycursor = con.cursor()
# Delete record
sql = "DELETE FROM users WHERE id = %s"
value = (3,)
mycursor.execute(sql, value)
con.commit()
print(mycursor.rowcount, "record deleted.")
con.close()