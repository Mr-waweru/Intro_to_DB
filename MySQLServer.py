import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Aa36997362",
    database = "DEMMO"
)

mycursor = mydb.cursor()

def create_database():
    try:
        query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        mycursor.execute(query)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    else:
        print("Database 'alx_book_store' created successfully!")
        

if __name__ == "__main__":
    create_database()