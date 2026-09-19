from connection import get_connection
con=get_connection()
mycursor = con.cursor()
# Data to insert
users = [
    ("John1", "john@gmail.com", "john123"),
    ("Alice1", "alice@gmail.com", "alice123"),
    ("Bob12", "bob1@gmail.com", "bob1213"),
    ("Emma11", "emma1@gmail.com", "emma1123")
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