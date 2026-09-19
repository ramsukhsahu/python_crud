from connection import get_connection
con=get_connection()
mycursor = con.cursor()
# Update record
sql = """
    UPDATE users
    SET name = %s, email = %s, password = %s
    WHERE id = %s
"""
values = ("Ajay Kumar", "ajay11@gmail.com", "ajay1234", 2)
mycursor.execute(sql, values)
con.commit()
print(mycursor.rowcount, "record updated.")
con.close()