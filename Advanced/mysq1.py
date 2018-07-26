import mysql.connector

# open connection
cnx = mysql.connector.connect(user='root', 
								password='1234',
                              	host='127.0.0.1',
                              	database='pythondb')

cursor = cnx.cursor()

# execute SQL statement: create, read, delete, update
# 1 create tabel 

sql = """CREATE TABLE EMPLOYEE ( 
	FIRST_NAME CHAR(20) NOT NULL,
	LAST_NAME CHAR(20), 
	AGE INT,
	SEX CHAR(1),
	INCOME FLOAT )"""
cursor.execute(sql)

# close connection
cnx.close()
