import mysql.connector

# open connection
cnx = mysql.connector.connect(user='root', 
								password='1234',
                              	host='127.0.0.1',
                              	database='pythondb')

cursor = cnx.cursor()

# 5. delete record
sql = """DELETE FROM EMPLOYEE
WHERE 
	AGE <= %d 
"""

try:
	cursor.execute(sql % (20,))
	cnx.commit()
except:
	cnx.rollback()
	print "statement rollback"


# close connection
cnx.close()
