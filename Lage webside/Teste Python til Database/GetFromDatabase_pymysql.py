import pymysql
def connect_to_databse():

# Connection to database
    database_SLS = "SpiceLogisticsSystems"
    db_user = "root"
    db_pwd = "password"
    php_host = "localhost/phpmyadmin/"
    php_port = 80

connection = pymysql.connect(
    host="localhost",
    port=3307,
    user="root",
    passwd="password",
    database="SpiceLogisticsSystems"
)



with connection:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `Student` WHERE `Studnr`=125"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)





