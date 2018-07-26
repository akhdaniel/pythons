import mysql.connector

# open connection
cnx = mysql.connector.connect(user='root', 
								password='1234',
                              	host='127.0.0.1',
                              	database='pythondb')

cursor = cnx.cursor()

# 4. update record
sql = """UPDATE EMPLOYEE
SET FIRST_NAME= '%s',
	LAST_NAME = '%s'
WHERE 
	FIRST_NAME='%s'
"""

try:
	cursor.execute(sql % ('Ade','Husain','Joko'))
	cnx.commit()
except:
	cnx.rollback()
	print "statement rollback"


# close connection
cnx.close()
