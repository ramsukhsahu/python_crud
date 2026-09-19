from connection import get_connection
con=get_connection()
mycursor = con.cursor()
# Data to insert
users = [
    ("Ram", "ram@gmail.com", "ram123"),
    ("Ajay", "ajay@gmail.com", "ajay1234"),
    ("vijay", "vijay@gmail.com", "vijay1123"),
    ("akash", "akash@gmail.com", "akash111")
]
# Insert multiple records
sql = """
    INSERT INTO users (name, email, password)
    VALUES (%s, %s, %s)
"""
mycursor.executemany(sql, users)
con.commit()
print(mycursor.rowcount, "records inserted.")
con.close()