from connection import get_connection
con=get_connection()
mycursor = con.cursor()
# Update record
sql = """
    UPDATE users
    SET name = %s, email = %s, password = %s
    WHERE id = %s
"""
values = ("John Smith333", "johnsmith33@gmail.com", "john456", 13)
mycursor.execute(sql, values)
con.commit()
print(mycursor.rowcount, "record updated.")
con.close()