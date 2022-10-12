import mysql.connector
from mysql.connector import Error

database_SLS = "SpiceLogisticsSystems"
db_user = "root"
db_pwd = "password"
db_host = "localhost"


try:
    connection = mysql.connector.connect(host=db_host,
                                         port = 3307,
                                         user="root",
                                         password="password",
                                         database=database_SLS
                                         )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
        print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")