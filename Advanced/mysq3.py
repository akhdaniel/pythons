import mysql.connector

# open connection
cnx = mysql.connector.connect(user='root', 
								password='1234',
                              	host='127.0.0.1',
                              	database='pythondb')

cursor = cnx.cursor()

# 3. read record
sql = """SELECT 
	FIRST_NAME, 
	LAST_NAME, 
	AGE, 
	SEX, 
	INCOME
FROM EMPLOYEE
WHERE 
	AGE > %d
"""

try:
	cursor.execute(sql % (20,))
	results = cursor.fetchall()
	for row in results:
		print row[0], row[1], row[2], row[3], row[4]

except:
	print "statement rollback"


# close connection
cnx.close()
