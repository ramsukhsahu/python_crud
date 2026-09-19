import mysql.connector

def get_connection():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="python_db"
        )

        #print("Connection successful!")
        return con

    except mysql.connector.Error as err:
        print("Connection failed!")
        print("Error:", err)
        return None


# Call the function
get_connection()