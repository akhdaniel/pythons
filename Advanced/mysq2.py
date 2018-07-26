import mysql.connector

# open connection
cnx = mysql.connector.connect(user='root', 
								password='1234',
                              	host='127.0.0.1',
                              	database='pythondb')

cursor = cnx.cursor()

# 2. insert record
sql = """INSERT INTO EMPLOYEE(
	FIRST_NAME, 
	LAST_NAME, 
	AGE, 
	SEX, 
	INCOME)
VALUES (
	'%s', 
	'%s', 
	%d, 
	'%s', 
	%d)"""

try:
	cursor.execute(sql % ('Joko', 'Dodo', 23, 'M', 2000  ) )
	cursor.execute(sql % ('Bowo', 'Didi', 33, 'M', 3000  ) )
	cnx.commit()
	print "statement commmit"
except:
	print "statement rollback"
	cnx.rollback()


# close connection
cnx.close()
