import mysql.connector

def sql_connection():
    return mysql.connector.connect (
        host = "localhost",
        user = "root",
        password = "SushiSql72!",
        database = "elite102_banking_app"
    )

if __name__ == "__main__":
    connection = sql_connection()
    print ("Working!")
    connection.close

