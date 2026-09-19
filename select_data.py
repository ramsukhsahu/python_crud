from connection import get_connection

con = get_connection()
mycursor = con.cursor()

# Fetch particular data have id 1 from database
# user_id = 1
# mycursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
# row = mycursor.fetchone()
# if row:
#     print("ID | Name | Email | Password")
#     print("-" * 50)
#     print(row[0], "|", row[1], "|", row[2], "|", row[3])
# else:
#     print("User not found")

# Fetch data from database
mycursor.execute("SELECT * FROM users")

rows = mycursor.fetchall()

print("ID | Name | Email | Password")
print("-" * 50)

for row in rows:
    print(row[0], "|", row[1], "|", row[2], "|", row[3])

con.close()